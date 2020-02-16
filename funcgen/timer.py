#!/usr/bin/env python

import sys,subprocess
import time

ip_address = 'ip address of the function generator'

timelimit = 0
if len(sys.argv)==2:
    timelimit = int(sys.argv[1])
    ch_list= ['1','2']
elif len(sys.argv)==3:
    timelimit = int(sys.argv[1])
    ch_list = [sys.argv[2]]
else:
    print('Usage: ./timer.py [pause (sec)]')
    print('Usage: ./timer.py [pause (sec)] [ch]')
    exit(1)

print('waiting...' + str(timelimit) + '(s)')
time.sleep(timelimit)
print('beep! beep!')

for ch in ch_list:
    cmd = './tek/utils/tek_afg/tek_afg -i %s E:%s:OFF' % (ip_address,ch)
    print(cmd)
    subprocess.check_output(cmd, shell=True)
