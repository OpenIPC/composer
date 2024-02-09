#!/bin/sh

(devmem 0x112c0048 32 0x0 ; sleep 1 ; gpio clear 71 ; sleep 1 ; gpio set 71 ; sleep 1) >/dev/null

ipctool2 i2cset 0x88 0x02 0xC8
ipctool2 i2cset 0x88 0x05 0x00
ipctool2 i2cset 0x88 0x06 0x32
ipctool2 i2cset 0x88 0x07 0xC0
ipctool2 i2cset 0x88 0x08 0x00
ipctool2 i2cset 0x88 0x09 0x24
ipctool2 i2cset 0x88 0x0A 0x48
ipctool2 i2cset 0x88 0x0B 0xC0
ipctool2 i2cset 0x88 0x0C 0x03
ipctool2 i2cset 0x88 0x0D 0x50
ipctool2 i2cset 0x88 0x0E 0x00
ipctool2 i2cset 0x88 0x0F 0x00
ipctool2 i2cset 0x88 0x10 0x00
ipctool2 i2cset 0x88 0x11 0x40
ipctool2 i2cset 0x88 0x12 0x60
ipctool2 i2cset 0x88 0x13 0x00
ipctool2 i2cset 0x88 0x14 0x00
ipctool2 i2cset 0x88 0x15 0x03
ipctool2 i2cset 0x88 0x16 0xD2
ipctool2 i2cset 0x88 0x17 0x80
ipctool2 i2cset 0x88 0x18 0x29
ipctool2 i2cset 0x88 0x19 0x38
ipctool2 i2cset 0x88 0x1A 0x47
ipctool2 i2cset 0x88 0x1B 0x01
ipctool2 i2cset 0x88 0x1C 0x08
ipctool2 i2cset 0x88 0x1D 0x98
ipctool2 i2cset 0x88 0x1E 0x80
ipctool2 i2cset 0x88 0x1F 0x80
ipctool2 i2cset 0x88 0x20 0x30
ipctool2 i2cset 0x88 0x21 0x84
ipctool2 i2cset 0x88 0x22 0x36
ipctool2 i2cset 0x88 0x23 0x3C
ipctool2 i2cset 0x88 0x24 0x04
ipctool2 i2cset 0x88 0x25 0xFF
ipctool2 i2cset 0x88 0x26 0x05
ipctool2 i2cset 0x88 0x27 0x2D
ipctool2 i2cset 0x88 0x28 0x00
ipctool2 i2cset 0x88 0x29 0x48
ipctool2 i2cset 0x88 0x2A 0x30
ipctool2 i2cset 0x88 0x2B 0x60
ipctool2 i2cset 0x88 0x2C 0x0A
ipctool2 i2cset 0x88 0x2D 0x30
ipctool2 i2cset 0x88 0x2E 0x70
ipctool2 i2cset 0x88 0x2F 0x00
ipctool2 i2cset 0x88 0x30 0x48
ipctool2 i2cset 0x88 0x31 0xBB
ipctool2 i2cset 0x88 0x32 0x2E
ipctool2 i2cset 0x88 0x33 0x90
ipctool2 i2cset 0x88 0x34 0x00
ipctool2 i2cset 0x88 0x35 0x05
ipctool2 i2cset 0x88 0x36 0xDC
ipctool2 i2cset 0x88 0x37 0x00
ipctool2 i2cset 0x88 0x38 0x00
ipctool2 i2cset 0x88 0x39 0x1C
ipctool2 i2cset 0x88 0x3A 0x32
ipctool2 i2cset 0x88 0x3B 0x26
ipctool2 i2cset 0x88 0x3C 0x00
ipctool2 i2cset 0x88 0x3D 0x60
ipctool2 i2cset 0x88 0x3E 0x00
ipctool2 i2cset 0x88 0x3F 0x00
ipctool2 i2cset 0x88 0x40 0x00
ipctool2 i2cset 0x88 0x41 0x00
ipctool2 i2cset 0x88 0x42 0x00
ipctool2 i2cset 0x88 0x43 0x00
ipctool2 i2cset 0x88 0x44 0x00
ipctool2 i2cset 0x88 0x45 0x00
ipctool2 i2cset 0x88 0x46 0x00
ipctool2 i2cset 0x88 0x47 0x00
ipctool2 i2cset 0x88 0x48 0x00
ipctool2 i2cset 0x88 0x49 0x00
ipctool2 i2cset 0x88 0x4A 0x00
ipctool2 i2cset 0x88 0x4B 0x00
ipctool2 i2cset 0x88 0x4C 0x43
ipctool2 i2cset 0x88 0x4D 0x00
ipctool2 i2cset 0x88 0x4E 0x17
ipctool2 i2cset 0x88 0x4F 0x00
ipctool2 i2cset 0x88 0x50 0x00
ipctool2 i2cset 0x88 0x51 0x00
ipctool2 i2cset 0x88 0x52 0x00
ipctool2 i2cset 0x88 0x53 0x00
ipctool2 i2cset 0x88 0x54 0x00

ipctool2 i2cset 0x88 0xB3 0xFA
ipctool2 i2cset 0x88 0xB4 0x00
ipctool2 i2cset 0x88 0xB5 0x00
ipctool2 i2cset 0x88 0xB6 0x00
ipctool2 i2cset 0x88 0xB7 0x00
ipctool2 i2cset 0x88 0xB8 0x00
ipctool2 i2cset 0x88 0xB9 0x00
ipctool2 i2cset 0x88 0xBA 0x00
ipctool2 i2cset 0x88 0xBB 0x00
ipctool2 i2cset 0x88 0xBC 0x00
ipctool2 i2cset 0x88 0xBD 0x00
ipctool2 i2cset 0x88 0xBE 0x00
ipctool2 i2cset 0x88 0xBF 0x00
ipctool2 i2cset 0x88 0xC0 0x00
ipctool2 i2cset 0x88 0xC1 0x00
ipctool2 i2cset 0x88 0xC2 0x0B
ipctool2 i2cset 0x88 0xC3 0x0C
ipctool2 i2cset 0x88 0xC4 0x00
ipctool2 i2cset 0x88 0xC5 0x00
ipctool2 i2cset 0x88 0xC6 0x1F
ipctool2 i2cset 0x88 0xC7 0x78
ipctool2 i2cset 0x88 0xC8 0x27
ipctool2 i2cset 0x88 0xC9 0x00
ipctool2 i2cset 0x88 0xCA 0x00
ipctool2 i2cset 0x88 0xCB 0x07
ipctool2 i2cset 0x88 0xCC 0x08
ipctool2 i2cset 0x88 0xCD 0x00
ipctool2 i2cset 0x88 0xCE 0x00
ipctool2 i2cset 0x88 0xCF 0x04
ipctool2 i2cset 0x88 0xD0 0x00
ipctool2 i2cset 0x88 0xD1 0x00
ipctool2 i2cset 0x88 0xD2 0x60
ipctool2 i2cset 0x88 0xD3 0x10
ipctool2 i2cset 0x88 0xD4 0x06
ipctool2 i2cset 0x88 0xD5 0xBE
ipctool2 i2cset 0x88 0xD6 0x39
ipctool2 i2cset 0x88 0xD7 0x27
ipctool2 i2cset 0x88 0xD8 0x00
ipctool2 i2cset 0x88 0xD9 0x00
ipctool2 i2cset 0x88 0xDA 0x00
ipctool2 i2cset 0x88 0xDB 0x00
ipctool2 i2cset 0x88 0xDC 0x00
ipctool2 i2cset 0x88 0xDD 0x00
ipctool2 i2cset 0x88 0xDE 0x00
ipctool2 i2cset 0x88 0xDF 0x00
ipctool2 i2cset 0x88 0xE0 0x00
ipctool2 i2cset 0x88 0xE1 0x00
ipctool2 i2cset 0x88 0xE2 0x00
ipctool2 i2cset 0x88 0xE3 0x00
ipctool2 i2cset 0x88 0xE4 0x00
ipctool2 i2cset 0x88 0xE5 0x00
ipctool2 i2cset 0x88 0xE6 0x00
ipctool2 i2cset 0x88 0xE7 0x13
ipctool2 i2cset 0x88 0xE8 0x03
ipctool2 i2cset 0x88 0xE9 0x00
ipctool2 i2cset 0x88 0xEA 0x00
ipctool2 i2cset 0x88 0xEB 0x00
ipctool2 i2cset 0x88 0xEC 0x00
ipctool2 i2cset 0x88 0xED 0x00
ipctool2 i2cset 0x88 0xEE 0x00
ipctool2 i2cset 0x88 0xEF 0x00
ipctool2 i2cset 0x88 0xF0 0x00
ipctool2 i2cset 0x88 0xF1 0x00
ipctool2 i2cset 0x88 0xF2 0x00
ipctool2 i2cset 0x88 0xF3 0x00
ipctool2 i2cset 0x88 0xF4 0x20
ipctool2 i2cset 0x88 0xF5 0x10
ipctool2 i2cset 0x88 0xF6 0x00
ipctool2 i2cset 0x88 0xF7 0x00
ipctool2 i2cset 0x88 0xF8 0x00
ipctool2 i2cset 0x88 0xF9 0x00
ipctool2 i2cset 0x88 0xFA 0x88
ipctool2 i2cset 0x88 0xFB 0x00
ipctool2 i2cset 0x88 0xFC 0x00

ipctool2 i2cset 0x88 0x40 0x08
ipctool2 i2cset 0x88 0x00 0x00
ipctool2 i2cset 0x88 0x01 0xf8
ipctool2 i2cset 0x88 0x02 0x01
ipctool2 i2cset 0x88 0x08 0xF0
ipctool2 i2cset 0x88 0x13 0x04
ipctool2 i2cset 0x88 0x14 0x73
ipctool2 i2cset 0x88 0x15 0x08
ipctool2 i2cset 0x88 0x20 0x12
ipctool2 i2cset 0x88 0x34 0x1b
ipctool2 i2cset 0x88 0x23 0x02
ipctool2 i2cset 0x88 0x23 0x00

ipctool2 i2cset 0x88 0x40 0x00
