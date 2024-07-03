#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
'''
Relevation Password Printer

A command line interface to Revelation Password Manager.

Code based on Revelation's former BTS (no longer online, not archived?).
''' # $Id$

# References:
# - (ref1) code:
#   http://oss.wired-networks.net/bugzilla/attachment.cgi?id=13&action=view
# - (ref2) bug report:
#   http://oss.wired-networks.net/bugzilla/show_bug.cgi?id=111
#   archived -> http://web.archive.org/http://oss.wired-networks.net/bugzilla/show_bug.cgi?id=111
# - (ref3) http://docs.python.org/library/zlib.html
# - (ref4) http://pymotw.com/2/getpass/

# Relevation Password Printer
#
# Copyright (c) 2011,2012,2013,2014,2020,2024 Toni Corvera
# All rights reserved.
#
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions are
# met:
# 1. Redistributions of source code must retain the above copyright
#    notice, this list of conditions and the following disclaimer.
# 2. Redistributions in binary form must reproduce the above copyright
#    notice, this list of conditions and the following disclaimer in the
#    documentation and/or other materials provided with the distribution.
#
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS"
# AND EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
# IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE
# ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE
# LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR
# CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF
# SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS
# INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN
# CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE)
# ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE
# POSSIBILITY OF SUCH DAMAGE.

# Allow type hints with subscripting (i.e. list[str]) in Python < 3.9
from __future__ import annotations

# __date__ = '$Date$'
# __revision__ = '$Rev$'

import argparse
import configparser
import getpass
from lxml import etree
import os
import stat
import sys
import textwrap
from dataclasses import dataclass
import zlib
import hashlib # required by newer format
# PBKDF2 stolen from Revelation
from . import PBKDF2, __version__, __author__, RELEASE
if not RELEASE:
    import traceback

try:
    from Cryptodome.Cipher import AES
except (ImportError, ModuleNotFoundError):
    sys.stderr.write('PyCryptodome is required\n')
    raise

# These are pseudo-standardized exit codes, in Linux (*NIX?) they are defined
#+in the header </usr/include/sysexits.h> and available as properties of 'os'
#+In windows they aren't defined at all, or partially (e.g. EX_OK is defined
#+in newer versions)

if 'EX_DATAERR' not in dir(os):
    # If not defined set them manually
    codes = { 'EX_OK': 0,       'EX_USAGE':    64, 'EX_DATAERR': 65,
              'EX_NOINPUT': 66, 'EX_SOFTWARE': 70, 'EX_IOERR': 74,
    }
    for (k,v) in list(codes.items()):
        setattr(os, k, v)
    del codes, k, v

TAGNAMES = {
    'generic-url': 'Url:',
    'generic-username': 'Username:',
    'generic-password': 'Password:',
    'generic-email': 'Email:',
    'generic-hostname': 'Hostname:',
    'generic-location': 'Location:',
    'generic-code': 'Code:',
    'generic-certificate': 'Certificate:',
    'generic-database': 'Database:',
    'generic-domain': 'Domain:',
    'generic-keyfile': 'Key file:',
    'generic-pin': 'PIN',
    'generic-port': 'Port'
}
MODE_AND = 'and'
MODE_OR = 'or'
PASS_SOURCE_ARG = 'arg'
PASS_SOURCE_ASK = 'ask'
PASS_SOURCE_STDIN = 'stdin'
KNOWN_TYPES = (
    'creditcard', 'cryptokey', 'database', 'door', 'email',
    'folder', 'ftp', 'generic', 'phone', 'shell', 'website'
)
# Used to wrap some informational text
CONSOLE_WIDTH: int = 80


# Errors
@dataclass(frozen=True)
class RlvError(Exception):
    msg: str
    exitCode: int = 1

    def __str__(self) -> str:
        return self.msg


@dataclass(frozen=True)
class DecryptError(RlvError):
    exitCode: int = os.EX_DATAERR
    msg: str = 'Failed to decrypt data. Wrong password?'


@dataclass(frozen=True)
class DecompressError(RlvError):
    exitCode: int = os.EX_DATAERR
    msg: str = 'Failed to decompress data.'


@dataclass(frozen=True)
class DataFormatError(RlvError):
    exitCode: int = os.EX_DATAERR
    msg: str = 'Incorrect data format'


@dataclass(frozen=True)
class DataVersionError(RlvError):
    exitCode: int  = os.EX_DATAERR
    msg: str = 'Data format version not supported'


def printe(s: str) -> None:
    ' Print to stderr '
    sys.stderr.write(s+'\n')


def generate_config(datafile: str, password: str, mode: str) -> None:
    ' Print config file to stdout, instructions to stderr, and exit '
    print('### Start of configuration ###', file=sys.stderr)
    if password:
        print(textwrap.fill(
            'The password is stored as plain text, you may prefer not to'
            ' include it for security reasons',
            width=CONSOLE_WIDTH,
            initial_indent='# ',
            subsequent_indent='# ',
        ))
    print('[relevation]')
    if datafile:
        print(f'file={os.path.realpath(datafile)}')
    if password:
        print(f'password={password}')
    print(f'mode={mode}')
    print('### End of configuration ###', file=sys.stderr)
    # TODO: Is this explanation close-enough for Windows?
    conf_path = get_config_path()
    print(textwrap.dedent(f'''
          Copy the generated configuration to {conf_path}, or rerun as:
          relevation --generate-config > {conf_path}
          '''),
          file=sys.stderr
    )
    sys.exit(os.EX_OK)


def make_xpath_query(search_text: str | list[str] = None,
                     type_filter: str = None,
                     ignore_case: bool = True,
                     negate_filter: bool = False) -> str:
    ''' Construct the actual XPath expression.

    Passing a list as the first argument implies combining its elements
    in the search (AND).
    '''
    xpath = '/revelationdata//entry'
    if type_filter:
        sign = '='
        if negate_filter:
            sign = '!='
        xpath = f'{xpath}[@type{sign}"{type_filter}"]'
        if type_filter != 'folder':
            # Avoid printing folders since all their children are printed
            # alongside
            xpath += '[@type!="folder"]'
    if search_text:
        # xpath = xpath + '//text()'
        # needles: str | list[str] = list()
        if isinstance(search_text, list):
            needles = search_text
        else:
            # FIXME: Used for OR's
            assert isinstance(search_text, str)
            needles = [ search_text, ]
        selector = ''
        for search in needles:
            if ignore_case:
                # must pass lowercase to actually be case insensitive
                search = search.lower()
                # XPath 2.0 has lower-case, upper-case, matches(..., -i) etc.
                selector += '//text()[contains(translate(.,'\
                            ' "ABCDEFGHIJKLMNOPQRSTUVWXYZ",'\
                            f' "abcdefghijklmnopqrstuvwxyz"), "{search}")]/../..'
            else:
                selector += f'//text()[contains(., "{search}")]/../..'
        xpath = f'{xpath}{selector}'
    if not RELEASE:
        printe(f'> Xpath: {xpath}\n')
    return xpath


def dump_all_entries(xmldata: bytes) -> int:
    ' Dump all entries from xmldata, with no filter at all '
    tree = etree.fromstring(xmldata)
    res = tree.xpath('//entry')
    return dump_result(res, 'all')


def dump_entries(xmldata: bytes,
                 search_text: str | list[str] = None,
                 type_filter: str = None,
                 ignore_case: bool = True,
                 negate_filter: bool = False) -> int:
    ''' Dump entries from xmldata that match criteria.
    '''
    tree = etree.fromstring(xmldata)
    xpath = make_xpath_query(search_text, type_filter, ignore_case, negate_filter)
    try:
        res = tree.xpath(xpath)
    except etree.XPathEvalError:
        if not RELEASE:
            printe(f'Failed with xpath expression: {xpath}')
        raise
    query_desc = ''
    if search_text:
        query_desc = f'"{search_text}"'
    if type_filter:
        neg = ''
        if negate_filter:
            neg = 'not '
        if search_text:
            query_desc = f'{query_desc} (\'{neg}{type_filter}\' entries)'
        else:
            query_desc = f'{neg}{type_filter} entries'
    nr = dump_result(res, query_desc)
    return nr


def dump_single_result(type_name: str, name: str, descr: str,
                       notes: str, fields: list[tuple[str, str]]) -> None:
    printe('-------------------------------------------------------------------------------')
    s: str = textwrap.dedent(f'''
            Type: {type_name}
            Name: {name}
            Description: {descr}
    ''')
    # Notes can be multiline so it would break the dedent above

    # pre-process notes to print them indented
    notes_list = notes.split('\n')
    if notes_list:
        s += f'Notes: {notes_list[0]}'
        s += textwrap.indent('\n'.join(notes_list[1:]), ' ') + '\n'

    for field,value in fields:
        s += f'{field} {value}\n'
    print(s)


def dump_result(res: list, query_desc: str, dumpfn=dump_single_result) -> int:
    ''' Print query results.
    
    :param res: list of entries
    :param query_desc: description of the query
    :param dumpfn: function to call for each entry
    '''
    print(f'-> Search {query_desc}: ', end=' ')
    if not len(res):
        print('No results')
        return False
    print(f'{len(res)} matches')
    for x in res:
        type_name = x.get('type')
        name = None
        descr = None
        fields = []
        notes = None
        for child in x.getchildren():
            tag = child.tag
            val = child.text or ''
            if tag == 'name':
                name = val
            elif tag == 'description':
                descr = val
            elif tag == 'field':
                idv = child.get('id')
                if idv in TAGNAMES:
                    idv = TAGNAMES[idv]
                # Maintain order => list
                fields += [(idv, val),]
            elif tag == 'notes':
                notes = val
        dumpfn(type_name, name, descr, notes, fields)
        # / for child in x.children
    nr = len(res)
    plural = ''
    if nr > 1:
        plural = 's'
    printe('-------------------------------------------------------------------------------')
    printe(f'<- (end of {nr} result{plural} for {{{query_desc}}})\n')
    return nr


def world_readable(path: str) -> bool:
    ' Check if a file is readable by everyone '
    assert os.path.exists(path)
    st = os.stat(path)
    return bool(st.st_mode & stat.S_IROTH)


def get_config_path() -> str:
    '''
    :return: Expected config file path (may or may not exist)
    '''
    return os.path.join(os.path.expanduser('~'), '.relevation.conf')


def load_config() -> tuple[str,str]:
    ''' Load configuration file if one is found.
    :return: (file, password, mode)
    '''
    cfg = get_config_path()
    pw = None
    fl = None
    mode = MODE_OR
    if os.path.isfile(cfg):
        if os.access(cfg, os.R_OK):
            parser = configparser.ConfigParser()
            parser.read(cfg)
            ops = parser.options('relevation')
            if 'file' in ops:
                fl = os.path.expanduser(parser.get('relevation', 'file'))
            if 'password' in ops:
                if world_readable(cfg):
                    printe(textwrap.fill(
                            f'Warning: Your password in the configuration file ({cfg})'
                            ' can be read by anyone!!!',
                            width=CONSOLE_WIDTH,
                            subsequent_indent=' '
                        )
                    )
                pw = parser.get('relevation', 'password')
            if 'mode' in ops:
                mode = parser.get('relevation', 'mode')
                if mode not in [ MODE_AND, MODE_OR ]:
                    printe(f'Warning: Unknown mode \'{mode}\' set in configuration')
                    mode=MODE_OR
        else: # exists but not readable
            printe(f'Configuration file ({cfg}) is not readable!')
    return ( fl, pw, mode )


class _DataReaderBase(object):
    ' Common methods for reading data files '
    def validate_compressed_padding(self, data: bytes) -> bool:
        ''' Checks that the gzip-compressed 'data' is padded correctly.
        '''
        padlen = data[-1]  # XXX: While on Python 2 we were using ord(data[-1]), ord(i), etc.
        for i in data[-padlen:]:
            if i != padlen:
                return False
        return True

    def validate_cipher_length(self, data: bytes) -> bool:
        ''' Checks that encrypted 'data' has an appropriate length.
        Encrypted data length must be a multiple of 16
        '''
        return (len(data) % 16 == 0)

    def _aes_decrypt_ecb(self, key: bytes, data: bytes) -> bytes:
        ''' Decrypt AES cipher text in ECB mode.

        :return: clear data
        '''
        c = AES.new(key, AES.MODE_ECB)
        return c.decrypt(data)

    def _aes_decrypt_cbc(self, key: bytes, iv: bytes, data: bytes) -> bytes:
        ''' Decrypt AES cipher text in CBC mode.

        :return: clear data
        '''
        c = AES.new(key, AES.MODE_CBC, iv)
        return c.decrypt(data)

    def get_xml(self, data: str, password: str) -> bytes:
        ''' Extract the XML contents from the encrypted and compressed input.

            Note data is encoded in UTF-8 but returned as `bytes` (because
            the XML parser is too easy to choke in that case).
            <http://lxml.de/parsing.html#python-unicode-strings>
        '''
        pass


class DataReaderV1(_DataReaderBase):
    ''' Data reading for Revelation data files in the original format.
    Old format header:
        [0:12) 12B header: "rvl" 0x00, 0x01, 0x00
        [12:28) 16B ECB encrypted IV (for CBC-encrypted data)
        [28:] CBC encrypted data
    '''
    def _decrypt_compressed_data(self, password: str, cipher_text: bytes) -> bytes:
        ''' Decrypt cipher_text using password.

        :return: decrypted gzipped xml
        '''
        # Minimum length of header
        if len(cipher_text) < 28:
            raise DataFormatError
        # Key <= Padded password, as a byte array
        # (PyCryptodome needs 'bytes' instead of 'str')
        key = password
        key += (chr(0) * (32 - len(password)))
        key = key.encode('utf-8')
        # Extract IV
        iv = self._aes_decrypt_ecb(key, cipher_text[12:28])
        # Skip IV
        cipher_text = cipher_text[28:]
        # Input strings for decrypt must be a multiple of 16 in length
        if not self.validate_cipher_length(cipher_text):
            raise DataFormatError
        # Decrypt data, CBC mode
        return self._aes_decrypt_cbc(key, iv, cipher_text)

    def get_xml(self, data: str, password: str) -> bytes:
        # Decrypt. Decrypted data is compressed
        cleardata_gz = self._decrypt_compressed_data(password, data)
        # Validate padding for decompression
        if not self.validate_compressed_padding(cleardata_gz):
            raise DataFormatError
        # Decompress actual data (15 is wbits [ref3] DON'T CHANGE, 2**15 is the (initial) buf size)
        padlen = cleardata_gz[-1]
        try:
            return zlib.decompress(cleardata_gz[:-padlen], 15, 2**15)
        except zlib.error:
            raise DecompressError


class DataReaderV2(_DataReaderBase):
    ''' Data reading for Revelation data files in the new format.
    New format header:
        [0:12) 12B header: "rvl" 0x00, 0x02, 0x00
        [12:20) 8B salt
        [20:36) 16B IV (for CBC-encrypted data)
        [36:] CBC encrypted data
    The encryption key is derived from the password and salt through the
    PBKDF2 module.
    '''
    def _decrypt_compressed_data(self, password: str, cipher_text: bytes) -> bytes:
        # Minimum length of header
        if len(cipher_text) < 36:
            raise DataFormatError
        salt = cipher_text[12:20]
        iv = cipher_text[20:36]
        key = PBKDF2.PBKDF2(password, salt, iterations=12000).read(32)
        # Skip encryption header
        cipher_text = cipher_text[36:]
        if not self.validate_cipher_length(cipher_text):
            raise DataFormatError
        # Decrypt data (CBC)
        decrypted = self._aes_decrypt_cbc(key, iv, cipher_text)
        sha256hash = decrypted[0:32]
        # Skip hash. decrypted <= Decrypted, Compressed data
        decrypted = decrypted[32:]
        # Validate hash
        if sha256hash != hashlib.sha256(decrypted).digest():
            raise DecryptError
        return decrypted

    def get_xml(self, data: bytes, password: str) -> bytes:
        # Decrypt...
        cleardata_gz = self._decrypt_compressed_data(password, data)
        # Validate padding for decompression
        if not self.validate_compressed_padding(cleardata_gz):
            raise DataFormatError
        # Decompress
        padlen = cleardata_gz[-1]
        try:
            return zlib.decompress(cleardata_gz[:-padlen])
        except zlib.error:
            raise DecompressError


class DataReader(object):
    ''' Interface to read Revelation's data files '''
    def __init__(self, filename: str) -> None:
        ''' Loads file data and checks file format and data version for compatibility

        :raises IOError: If `filename` not readable
        :raises DataFormatError: If `filename` not in Revelation format
        :raises DataVersionError: If `filename` not in a supported data format version
        '''
        self._impl = None
        self._data = None
        self._filename = filename
        if not os.access(filename, os.R_OK):
            raise IOError(f'File \'{filename}\' not accessible')
        with open(filename, 'rb') as f:
            # Encrypted data
            self._data = f.read()
        self._check_header()

    def _check_header(self) -> None:
        ''' Checks the file header for compatibility.

        :raises DataFormatError: If the file isn't a Revelation data file
        :raises DataVersionError: If the data format is in an unsupported version
        '''
        header = self._data[0:12]
        magic = header[0:4]
        if magic != b"rvl\x00":
            raise DataFormatError
        data_version = header[4]
        app_version = header[6:9]
        if data_version == 0x01:  # '\x01':
            self._impl = DataReaderV1()
        elif data_version == 0x02:  # '\x02':
            self._impl = DataReaderV2()
        else:
            raise DataVersionError

    def get_xml(self, password: str) -> bytes:
        ''' Decrypt and decompress file data.
        '''
        return self._impl.get_xml(self._data, password)


def parse_command_line(default_file: str,
                       default_password: str,
                       default_mode: str) -> tuple[argparse.ArgumentParser, argparse.Namespace]:
    # Note exit_on_error=False only deals with wrong arguments, not
    # unrecognized options, the old behaviour (printing help to stderr and
    # exiting with os.EX_USAGE) can't be reproduced
    parser = argparse.ArgumentParser(
                    #prog=sys.argv[0],
                    # Customize the help message manually
                    add_help=False,
                    allow_abbrev=False,
             )
    # Note that if --search targeted args.search we'd get only one of them or,
    # if using append on the positional argument, a list of strs (positional)
    # and a sublist (--search)
    parser.add_argument('SEARCH', nargs='*', help='Search for string.')
    parser.add_argument('-f', '--file', help='Revelation password file.')
    parser.add_argument('-p', '--password', metavar='PASS',
                        help='Master password.')
    parser.add_argument('-s', '--search', default=[],
                        action='append',
                        help='Search for string (deprecated).')
    parser.add_argument('-i', '--case-insensitive', dest='case_insensitive',
                        action='store_true',
                        help='Case insensitive search (default).')
    parser.add_argument('-c', '--case-sensitive', dest='case_insensitive',
                        action='store_false', help='Case sensitive search.')
    parser.add_argument('-a', '--ask', dest='pass_source',
                        action='store_const', const=PASS_SOURCE_ASK,
                        help='Interactively ask for password.')
    # Note unknown are accepted for historical reasons
    parser.add_argument('-t', '--type', action='append', type=str.lower,
                        help='Print only entries of type TYPE.\n'
                             'With no search string, prints all entries of'
                             ' type TYPE.')
    parser.add_argument('-A', '--and', dest='mode', action='store_const',
                        const=MODE_AND,
                        help='When multiple search terms are used, use an AND'
                             ' operator to combine them.')
    parser.add_argument('-O', '--or', dest='mode', action='store_const',
                        const=MODE_OR,
                        help='When multiple search terms are used, use an OR'
                             ' operator to combine them (default).')
    parser.add_argument('-x', '--xml', action='store_true',
                        help='Dump unencrypted XML document.')
    parser.add_argument('-0', '--stdin', dest='pass_source',
                        action='store_const', const=PASS_SOURCE_STDIN,
                        help='Read password from standard input.')
    parser.add_argument('--generate-config', action='store_true',
                        help='Prints a config file and instructions.')
    parser.add_argument('-h', '--help', action='help',
                        help='Print help (this message).')
    parser.add_argument('--version', action='store_true',
                        help='Print the program\'s version information.')
    parser.set_defaults(case_insensitive=True,
                        mode=default_mode,
                        pass_source=PASS_SOURCE_ARG,
                        file=default_file,
                        password=default_password,
    )
    args = parser.parse_args()
    args.search = args.SEARCH + args.search
    return (parser,args)


def handle_argument_error(parser: argparse.ArgumentParser, errors: list[str]) -> None:
    ''' Handle the case of incorrect command-line arguments

    :param parser: The main parser object
    :param errors: Any errors to be displayed to the user
    '''
    err = argparse.ArgumentParser(parents=[parser,], add_help=False,
                                  epilog='\n'.join(errors),
                                  formatter_class=argparse.RawDescriptionHelpFormatter)
    err.print_help(sys.stderr)


def main() -> None:
    # individual search: ( 'value to search', 'type of search', 'type of entry to filter' )
    searchTypes = []

    printe(f'Relevation v{__version__}, (c) 2011-2024 Toni Corvera\n')

    # ---------- OPTIONS ---------- #
    ( cfg_file, cfg_password, cfg_mode ) = load_config()
    ( arg_parser, args ) = parse_command_line(cfg_file, cfg_password, cfg_mode)

    if args.version:
        import Cryptodome
        release='' if RELEASE else ' [DEBUG]'
        print(f'Relevation version {__version__}{release}')
        print(f'Python version {sys.version}')
        print(f'PyCryptodome version {Cryptodome.__version__}')
        sys.exit(os.EX_OK)

    if args.pass_source in (PASS_SOURCE_ASK,PASS_SOURCE_STDIN):
        prompt = ''
        if args.pass_source == PASS_SOURCE_ASK:
            prompt = 'File password: '
        # see [ref4]
        if sys.stdin.isatty():
            args.password = getpass.getpass(prompt=prompt, stream=sys.stderr)
        else:
            # Not a terminal, getpass won't work
            args.password = sys.stdin.readline();
            args.password = args.password[:-1] # XXX: would .rstrip() be safe enough?
    
    if args.generate_config:
        generate_config(args.file, args.password, args.mode)
        sys.exit(os.EX_OK)
    
    if not args.file or not args.password:
        errors = ['Fatal errors:',
                  '-------------'
        ]
        if not args.file:
            errors.append('  Input password filename is required')
        if not args.password:
            errors.append('  Password is required')
        handle_argument_error(arg_parser, errors)
        sys.exit(os.EX_USAGE)  
    
    if args.type:
        for arg in args.type:
            neg = False
            if arg.startswith('-'):
                arg = arg[1:]
                if len(arg) == 0:
                    continue
                neg = True
            if not arg in KNOWN_TYPES:
                printe(f'Warning: Type "{arg}" is not known by relevation.')
            searchTypes.append( ( arg, neg ) ) 
    
    # ---------- PASSWORDS FILE DECRYPTION AND DECOMPRESSION ---------- #
    xmldata = DataReader(args.file).get_xml(args.password)
    
    # ---------- QUERIES ---------- #
    if args.xml:
        print(xmldata.decode('utf8'))
        sys.exit(os.EX_OK)
    # Multiply values to search by type of searches
    numhits = 0

    if not ( args.search or searchTypes ): # No search nor filters, print all
        numhits = dump_all_entries(xmldata)
    elif not searchTypes: # Simple case, all searches are text searches
        if args.mode == MODE_OR:
            for text in args.search:
                numhits += dump_entries(xmldata, text, 'folder', args.case_insensitive, True)
        else:
            assert args.mode == MODE_AND, "Unknown boolean operation mode"
            numhits += dump_entries(xmldata, args.search, 'folder', args.case_insensitive, True)
    elif args.search:
        if args.mode == MODE_OR: # Do a search filtered for each type
            for text in args.search:
                for ( sfilter, negate ) in searchTypes:
                    numhits += dump_entries(xmldata, text, sfilter, args.case_insensitive,
                                    negate_filter=negate)
        else: # Do a combined search, filter for each type
            assert args.mode == MODE_AND, "Unknown boolean operation mode"
            for ( sfilter, negate ) in searchTypes:
                numhits += dump_entries(xmldata, args.search, sfilter, args.case_insensitive,
                                    negate_filter=negate)
    else: # Do a search only of types
        for ( sfilter, negate ) in searchTypes:
            numhits += dump_entries(xmldata, None, sfilter, negate_filter=negate)
    if numhits == 0:
        sys.exit(80)


def entrypoint() -> None:
    '''
    Entrypoint for script generation via hatch. MUST not take arguments
    '''
    try:
        main()
    except RlvError as e:
        printe(f'Error: {e.msg}')
        if not RELEASE:
            traceback.print_exc()
        sys.exit(e.exitCode)
    except etree.XMLSyntaxError as e:
        printe('XML parsing error')
        if not RELEASE:
            traceback.print_exc()
        sys.exit(os.EX_DATAERR)
    except IOError as e:
        if not RELEASE:
            traceback.print_exc()
        printe(str(e))
        sys.exit(os.EX_IOERR)


if __name__ == '__main__':
    entrypoint()

# vim:set ts=4 et ai fileencoding=utf-8: #
