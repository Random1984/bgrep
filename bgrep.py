#!/usr/bin/python
# -*- coding: utf-8 -*-

# Python 2.x

# a simple binary grep utility

import os, glob, mmap, shutil, sys, array

if len(sys.argv)!=2:
    print "usage: bgrep.py hex_string"
    print "example of hex_string: 001122aabb"
    exit(0)

pattern=array.array('B', sys.argv[1].decode("hex"))

for dir, subdir, files in os.walk(os.getcwd()):
    for file in files: 
        try:
            fullfname=dir+"/"+file
            fp = open(fullfname, 'r+')
            if os.stat(fp.name).st_size > 0:
                #print ("processing %s" % fp.name)
                mm = mmap.mmap(fp.fileno(), os.stat(fp.name).st_size)
                if mm.find(pattern, 0)!=-1:
                    sys.stdout.write ("[%s] pattern found\n" % fp.name)
                    sys.stdout.flush()
                mm.close()
        except IOError:
            sys.stderr.write ("%s: IOError\n" % fullfname)
