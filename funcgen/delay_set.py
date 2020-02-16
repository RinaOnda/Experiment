#!/usr/bin/env python

import sys, subprocess

ip_address = 'ip address of the function generator'

if len(sys.argv) == 2:
    ch_list = ['1', '2']
elif len(sys.argv) == 3:
    ch_list = [sys.argv[2]]
else:
    print('Usage: ./delay_set.py [Delay (ns)]')
    print('Usage: ./delay_set.py [Delay (ns)] [ch]')
    exit(1)

delay_set = float(sys.argv[1])

for ch in ch_list:
    cmd = './tek/utils/tek_afg/tek_afg -i %s -d \"SOUR%s:PULS:DEL %.2fns\"' % (ip_address, ch, delay_set)
    print(cmd)
    subprocess.check_output(cmd, shell=True)
