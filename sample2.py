#! /usr/bin/env python
import mmap
import os
import struct
import time
import ctypes
# Open the file for reading
fd = os.open('/tmp/mmaptest', os.O_RDWR)

# Memory map the file
buf = mmap.mmap(fd, mmap.PAGESIZE, mmap.MAP_SHARED, mmap.PROT_READ | mmap.PROT_WRITE)
i= None
s = None
offset=0
print "going to unapack"
        #new_i, = struct.unpack('i', buf[:4])
new_s, = struct.unpack('100s', buf[0:100])
array=new_s.split(',')
print array[0],array[1]

"""
        if s != new_s:
            #print 'i: %s => %d' % (i, new_i)
            print 's: %s => %s' % (s, new_s)
            print 'Press Ctrl-C to exit'
            #i = new_i
            s = new_s

        time.sleep(1)

"""


