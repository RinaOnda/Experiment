#!/usr/bin/env python

import sys, subprocess

ip_address = 'ip address of the function generator'

if len(sys.argv) == 2:
    ch_list = ['1', '2']
elif len(sys.argv) == 3:
    ch_list = [sys.argv[2]]
else:
    print('Usage: ./high_set.py [High (V)]')
    print('Usage: ./high_set.py [High (V)] [ch]')
    exit(1)

high_set = float(sys.argv[1])

for ch in ch_list:
    cmd = './tek/utils/tek_afg/tek_afg -i %s -d \"SOUR%s:VOLT:LEV:IMM:HIGH %.2fV\"' % (ip_address, ch, high_set)
    print(cmd)
    subprocess.check_output(cmd, shell=True)
