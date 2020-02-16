#!/usr/bin/env python

import sys, subprocess

ip_address = 'ip address of the function generator'

if len(sys.argv) == 2:
    ch_list = ['1', '2']
elif len(sys.argv) == 3:
    ch_list = [sys.argv[2]]
else:
    print('Usage: ./edge_set.py [Leading/Trailing Edge (ns)]')
    print('Usage: ./edge_set.py [Leading/Trailing Edge (ns)] [ch]')
    exit(1)

edge_set = float(sys.argv[1])

for ch in ch_list:
    if edge_set < 2.5:
        print('Leading/Trailing is too short! (<', 2.5, ' ns')
        exit(1)

    cmd = './tek/utils/tek_afg/tek_afg -i %s -d \"SOUR%s:PULS:TRAN:LEAD %.1fns\"' % (ip_address, ch, edge_set)
    print(cmd)
    subprocess.check_output(cmd, shell=True)
    cmd = './tek/utils/tek_afg/tek_afg -i %s -d \"SOUR%s:PULS:TRAN:TRA %.1fns\"' % (ip_address, ch, edge_set)
    print(cmd)
    subprocess.check_output(cmd, shell=True)
