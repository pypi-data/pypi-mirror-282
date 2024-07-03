#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""
Relevation Password Printer

A command line interface to Revelation Password Manager.
""" # $Id$
# Relevation Password Printer
#
# Copyright (c) 2011,2012,2013,2014,2024 Toni Corvera
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

__author__ = 'Toni Corvera'
# __date__ = '$Date$'
# __revision__ = '$Rev$'

# hatch appears to read __version__ directly so it can't be derived
# Relevation versioning:
#  - major and minor are always present, when micro is 0 it is dropped, i.e. 1.0.0 would become 1.0
#  Deprecated style
#  - pre-releases have a suffix .0-pre.NUMBER (>= 1)
#  New style (follows python conventions more closely and can be controlled by hatch)
#  - pre-releases have a suffix rcNUMBER (>= 0)
__version__ = '1.4rc0'
__version_info__ = __version__.split('.')
RELEASE='rc' not in __version__
if not RELEASE:
   main,pre = __version__.split('rc')
   __version_info__ = main.split('.')[:3] + ['rc%s' % pre,]
   del main,pre
__version_info__ = tuple(__version_info__)

# vim:set ts=4 et ai fileencoding=utf-8: #
