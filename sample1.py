#!/usr/bin/env python
import ctypes
import mmap
import os
import struct


def main():



    # Create new empty file to back memory map on disk
    fd = os.open('/tmp/mmaptest', os.O_CREAT | os.O_TRUNC | os.O_RDWR)

    # Zero out the file to insure it's the right size
    os.write(fd, '00' * mmap.PAGESIZE)     
    # Create the mmap instace with the following params:
    # fd: File descriptor which backs the mapping or -1 for anonymous mapping
    # length: Must in multiples of PAGESIZE (usually 4 KB)
    # flags: MAP_SHARED means other processes can share this mmap
    # prot: PROT_WRITE means this process can write to this mmap
    buf = mmap.mmap(fd, mmap.PAGESIZE, mmap.MAP_SHARED, mmap.PROT_WRITE)
    # Before we create a new value, we need to find the offset of the next free
    # memory address within the mmap
    offset = 0

    # Now ceate a string containing by first creating a c_char array
    s_type = ctypes.c_char * len(buf[:100])
    # Now create the ctypes instance
    s = s_type.from_buffer(buf, offset)

    print 'First 100 bytes of memory mapping: %r' % buf[:100]
    print 'Changing s'
    new_s = raw_input ('Enter a new value for s:')
    s.raw = new_s
    print 'First 100 bytes of memory mapping: %r' % buf[:100]
 

if __name__ == '__main__':
    main()
