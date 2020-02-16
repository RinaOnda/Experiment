#!/usr/bin/env python

import sys, subprocess

ip_address = 'ip address of the function generator'

def get_output(cmd, ch):
    cmd = cmd.replace('__CH__', ch)
    cmd_str = '~/tek/utils/tek_afg_read/tek_afg_read -i %s -d %s' % (ip_address, cmd)
    output = subprocess.check_output(cmd_str, shell=True)
    return output.split()[0]

if len(sys.argv) == 2:
    ch_list = ['1', '2']
elif len(sys.argv) == 3:
    ch_list = [sys.argv[2]]
else:
    print 'Usage: ./amplitude_set.py [Amplitude (V)]'
    print 'Usage: ./amplitude_set.py [Amplitude (V)] [ch]'
    exit(1)

amp_set = float(sys.argv[1])

for ch in ch_list:
	cmd = './tek/utils/tek_afg/tek_afg -i %s -d \"SOUR%s:VOLT:LEV:AMPL %.2f\"' % (ip_address, ch, amp_set)
	print cmd
	subprocess.check_output(cmd, shell=True)
