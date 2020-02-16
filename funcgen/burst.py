#!/usr/bin/env python

import sys, subprocess

ip_address = 'ip address of the function generator'

Ncycle = 0;
if len(sys.argv) == 2:
    ch_list = ['1', '2']
elif len(sys.argv) == 3:
    if int(sys.argv[2]) > 1:
    	ch_list = ['1', '2']
	Ncycle = int(sys.argv[2])
    else:
    	ch_list = [sys.argv[2]]
elif len(sys.argv) == 4:
    ch_list = [sys.argv[2]]
    Ncycle = int(sys.argv[3])
else:
    print 'Usage: ./burst.py [ON:1, OFF:0]'
    print 'Usage: ./burst.py [ON:1, OFF:0] [ch]'
    print 'Usage: ./burst.py [ON:1, OFF:0] [Ncycle]'
    print 'Usage: ./burst.py [ON:1, OFF:0] [Ncycle] [ch]'
    exit(1)

switch = int(sys.argv[1])

for ch in ch_list:
    if switch==1:
	cmd = './tek/utils/tek_afg/tek_afg -i %s -d \"SOUR%s:BURS:STAT ON\"' % (ip_address, ch)
    else:
	cmd = './tek/utils/tek_afg/tek_afg -i %s -d \"SOUR%s:BURS:STAT OFF\"' % (ip_address, ch)
	
    print(cmd)
    subprocess.check_output(cmd, shell=True)

if Ncycle>0:
    for ch in ch_list:
	cmd = './tek/utils/tek_afg/tek_afg -i %s -d \"SOUR%s:BURS:NCYC %s\"' % (ip_address,ch,Ncycle)
	print(cmd)
	subprocess.check_output(cmd, shell=True)
