#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Arabic-roots class
#  
#  Copyright 2018 zerrouki <zerrouki@majd4>
#  
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 2 of the License, or
#  (at your option) any later version.
#  
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#  
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software
#  Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#  MA 02110-1301, USA.
#  
#  
from __future__ import (
    absolute_import,
    print_function,
    unicode_literals,
    division,
    )
import roots_const
import re
   

def is_root(word):
    """ test if word is a root"""
    return word in roots_const.ROOTS
def stats():
    """ show root dictionary stats"""
    stat={"size":len(roots_const.ROOTS),
        "3 letters":len([x for x in roots_const.ROOTS if len(x) == 3]),
        "4 letters":len([x for x in roots_const.ROOTS if len(x) == 4]),
        }
    return stat;
def test(args):
    word = u"علم"
    print(is_root(word))
    print stats()
    
if __name__ == '__main__':
    test()
