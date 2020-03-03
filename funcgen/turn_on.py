#!/usr/bin/env python

import sys,subprocess

ip_address = 'ip address of the function generator'


if len(sys.argv)==1:
    ch_list= ['1','2']
elif len(sys.argv)==2:
    ch_list = [sys.argv[1]]
else:
    print('Usage: ./turn_on.py')
    print('Usage: ./turn_on.py [ch]')
    exit(1)

for ch in ch_list:
    cmd = '~/tek/utils/tek_afg/tek_afg -i %s E:%s:ON' % (ip_address,ch)
    print(cmd)
    subprocess.check_output(cmd, shell=True)
