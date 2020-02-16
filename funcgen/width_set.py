#!/usr/bin/env python

import sys, subprocess

ip_address = 'ip address of the function generator'

def get_output(cmd, ch):
    cmd = cmd.replace('__CH__', ch)
    cmd_str = './tek/utils/tek_afg_read/tek_afg_read -i %s -d %s' % (ip_address, cmd)
    output = subprocess.check_output(cmd_str, shell=True)
    return output.split()[0]

if len(sys.argv) == 2:
    ch_list = ['1', '2']
elif len(sys.argv) == 3:
    ch_list = [sys.argv[2]]
else:
    print('Usage: ./width_set.py [Width (ns)]')
    print('Usage: ./width_set.py [Width (ns)] [ch]')
    exit(1)

w_set = float(sys.argv[1])

for ch in ch_list:
    print('set width of channel ', ch)
    freq = float(get_output('SOUR__CH__:FREQ:FIX?', ch))/1000
    w_max = 1.0/freq * 1e6 * 0.999
    w_min = 1.0/freq * 1e6 * 0.001
    if w_set > w_max:
        print('Width is too long! (>', w_max, ' ns @ ', freq, 'kHz)')
        exit(1)
    if w_set < w_min:
        print('Width is too short! (<', w_min, ' ns @ ', freq, 'kHz)')
        exit(1)

    cmd = '~/tek/utils/tek_afg/tek_afg -i %s -d \"SOUR%s:PULS:WIDT %.1fns\"' % (ip_address, ch, w_set)
    print(cmd)
    #subprocess.check_output(cmd, shell=True)
