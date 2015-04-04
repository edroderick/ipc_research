#!/usr/bin/env python

from ctypes import Structure,c_uint16,c_double,c_ubyte,c_uint32,c_int16,c_char

CONTROLLER_REF_NAME = 'ipc-chan'

class CONTROLLER_REF(Structure):
    _pack_ = 1
    _fields_ = [("msg", c_char)]
                
