#!/usr/bin/env python

import subprocess

ip_address = 'ip address of the function generator'

cmd_list = [
    ['Status (0:OFF,1:ON)    ', 'OUTP__CH__:STAT?'], 
    ['Burst mode (0:OFF,1:ON)', 'SOUR__CH__:BURS?'], 
    ['  type                 ', 'SOUR__CH__:BURS:MODE?'], 
    ['  cycle                ', 'SOUR__CH__:BURS:NCYC?'], 
    ['Function               ', 'SOUR__CH__:FUNC?'],
    ['Frequency (Hz)         ', 'SOUR__CH__:FREQ:FIX?'],
    ['Delay (sec)            ', 'SOUR__CH__:PULS:DEL?'],
    ['Width (sec)            ', 'SOUR__CH__:PULS:WIDT?'],
    ['Leading Edge (sec)     ', 'SOUR__CH__:PULS:TRAN:LEAD?'],
    ['Trailing Edge (sec)    ', 'SOUR__CH__:PULS:TRAN:TRA?'],
    ['Offset (V)             ', 'SOUR__CH__:VOLT:LEV:OFFS?'],
    ['Amplitude (V)          ', 'SOUR__CH__:VOLT:LEV:AMPL?'],
    ['Duty (%)               ', 'SOUR__CH__:PULS:DCYC?']
]

def get_output(cmd, ch):
    cmd = cmd.replace('__CH__', ch)
    cmd_str = './tek/utils/tek_afg_read/tek_afg_read -i %s -d %s' % (ip_address, cmd)
    output = subprocess.check_output(cmd_str, shell=True)
    return output.split()[0]

for ch in ['1', '2']:
    print('***** Ch%s *****' % ch)
    for cmd in cmd_list:
        print(cmd[0], ':  ', get_output(cmd[1], ch))
