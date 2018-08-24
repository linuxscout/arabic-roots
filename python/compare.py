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
import pyarabic.araby as araby
import argparse

def normalize(word):
    """ normalize root"""
    
    nrm = araby.normalize_hamza(word)
    nrm = nrm.replace(araby.ALEF, araby.WAW)
    return nrm
def grabargs():
    parser = argparse.ArgumentParser(description='Lookup for existant roots.')
    # add file name to import and filename to export
    
    parser.add_argument("-f", dest="filename", required=True,
    help="input file" , metavar="FILE")
    
    args = parser.parse_args()
    return args
def test():
    args =grabargs()
    filename = args.filename
    cpt = 0
    cpt_not = 0
    list_roots =[]
    with open(filename) as myfile:
        for line in myfile:
            line = line.decode('utf8').strip('\n')
            tokens = araby.tokenize(line)
            tokens = [normalize(x) for x in tokens]
            tokens = [x for x in tokens if 3 <= len(x) <=4]
            list_roots.extend(tokens)
    # set uniq
    list_roots = set(list_roots)
    rootexistants= set(roots_const.ROOTS)
    diff = list(list_roots -rootexistants)
    cpt_not = len(diff)
    cpt = len(list_roots & rootexistants)
    
    #~ for root in list_roots:
        #~ if root not in roots_const.ROOTS:
            #~ print(root.encode('utf8'))
            #~ cpt_not +=1
        #~ else:
            #~ cpt += 1

    print("#list root %d, found %d\n# not found %d"%(len(list_roots), cpt,cpt_not))
    print(u"\n".join(diff).encode('utf8'))
    
if __name__ == '__main__':
    test()
