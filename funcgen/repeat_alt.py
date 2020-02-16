#!/usr/bin/env python

#repeat to turn on/off channels alternatively 

import sys,subprocess
import time

ip_address = 'ip address of the function generator'

ch_list = ['1', '2']
nrep = 1
pause = 0
if len(sys.argv)==1:
    nrep = 1
    pause = 0
elif len(sys.argv)==2:
    nrep = int(sys.argv[1])
    pause = 0
elif len(sys.argv)==3:
    nrep = int(sys.argv[1])
    pause = int(sys.argv[2])
else:
    print('Usage: ./repeat_alt.py')
    print('Usage: ./repeat_alt.py [nrepeat]')
    print('Usage: ./repeat_alt.py [nrepeat] [pause (sec)]')
    exit(1)

for i in range(nrep):
    print('processing ' + str(i) + '/' + str(nrep))
    for ch in ch_list:
	cmd = './tek/utils/tek_afg/tek_afg -i %s E:%s:ON' % (ip_address,ch)
	print(cmd)
	subprocess.check_output(cmd, shell=True)
	print('waiting...' + str(pause) + ' second')
	time.sleep(pause)
	cmd = './tek/utils/tek_afg/tek_afg -i %s E:%s:OFF' % (ip_address,ch)
	print(cmd)
	subprocess.check_output(cmd, shell=True)
	time.sleep(3)

