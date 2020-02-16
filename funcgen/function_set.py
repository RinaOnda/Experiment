#!/usr/bin/env python

import sys, subprocess

ip_address = 'ip address of the function generator'

if len(sys.argv) == 2:
    ch_list = ['1', '2']
elif len(sys.argv) == 3:
    ch_list = [sys.argv[2]]
else:
    print('Usage: ./function_set.py [SIN:0, SQU:1, RAMP:2, PULS:3, NOIS:4, DC:5, USER:6]')
    print('Usage: ./function_set.py [SIN:0, SQU:1, RAMP:2, PULS:3, NOIS:4, DC:5, USER:6] [ch]')
    exit(1)

switch = int(sys.argv[1])

for ch in ch_list:
    if switch==0:
	cmd = './tek/utils/tek_afg/tek_afg -i %s -d \"SOUR%s:FUNC:SHAP SIN\"' % (ip_address, ch)
    elif switch==2:
	cmd = './tek/utils/tek_afg/tek_afg -i %s -d \"SOUR%s:FUNC:SHAP SQU\"' % (ip_address, ch)
    elif switch==3:
	cmd = './tek/utils/tek_afg/tek_afg -i %s -d \"SOUR%s:FUNC:SHAP RAMP\"' % (ip_address, ch)
    elif switch==4:
	cmd = './tek/utils/tek_afg/tek_afg -i %s -d \"SOUR%s:FUNC:SHAP PULS\"' % (ip_address, ch)
    elif switch==5:
	cmd = './tek/utils/tek_afg/tek_afg -i %s -d \"SOUR%s:FUNC:SHAP NOIS\"' % (ip_address, ch)
    elif switch==6:
	cmd = './tek/utils/tek_afg/tek_afg -i %s -d \"SOUR%s:FUNC:SHAP DC\"' % (ip_address, ch)
    elif switch==7:
	cmd = './tek/utils/tek_afg/tek_afg -i %s -d \"SOUR%s:FUNC:SHAP USER\"' % (ip_address, ch)
    else:
        print('no function is assigned.')
	
    print(cmd)
    subprocess.check_output(cmd, shell=True)
