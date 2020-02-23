#!/usr/bin/env python

import os, sys, subprocess
import time

ip_address = 'ip address of your device'
OUTPUTFOLDER = './'
OUTPUTFILE = OUTPUTFOLDER + 'wf.txt'

start = time.time()
if len(sys.argv) == 3:
    ch = sys.argv[1]
    nEvent = int(sys.argv[2])
elif len(sys.argv) == 4:
    ch = sys.argv[1]
    nEvent = int(sys.argv[2])
    OUTPUTFILE = sys.argv[3]
else:
    print('Usage: ./wf_transfer.py [ch] [nEvent]')
    print('Usage: ./wf_transfer.py [ch] [nEvent] [outputfile]')
    exit(1)

#initialize
stp = 1
enp = stp + 999# + 2
cmd = '~/tek/utils/tek_afg/tek_afg -i %s -d \"CH%s:POS 0\"' % (ip_address, ch)
subprocess.check_output(cmd, shell=True)
cmd = '~/tek/utils/tek_afg/tek_afg -i %s -d \"DAT:SOU CH%s\"' % (ip_address, ch)
subprocess.check_output(cmd, shell=True)
cmd = '~/tek/utils/tek_afg/tek_afg -i %s -d \"DAT:ENC ASCI\"' % (ip_address)
subprocess.check_output(cmd, shell=True)
cmd = '~/tek/utils/tek_afg/tek_afg -i %s -d \"WFMO:BYT_N 1\"' % (ip_address)
subprocess.check_output(cmd, shell=True)
cmd = '~/tek/utils/tek_afg/tek_afg -i %s -d \"DAT:STAR %d\"' % (ip_address, stp)
subprocess.check_output(cmd, shell=True)
cmd = '~/tek/utils/tek_afg/tek_afg -i %s -d \"DAT:STOP %d\"' % (ip_address, enp)
subprocess.check_output(cmd, shell=True)
cmd = '~/tek/utils/tek_afg/tek_afg -i %s -d \"HOR:SCA 4e-6\"' % (ip_address) #set horizontal scale
subprocess.check_output(cmd, shell=True)
#cmd = '~/tek/utils/tek_afg/tek_afg -i %s -d \"ACQ:MOD AVE\"' % (ip_address)
#subprocess.check_output(cmd, shell=True)
#cmd = '~/tek/utils/tek_afg/tek_afg -i %s -d \"ACQ:NUMAV 256\"' % (ip_address)
#subprocess.check_output(cmd, shell=True)
#cmd = '~/tek/utils/tek_afg_read/tek_afg_read -i %s -d \"WFMO:NR_P?\"' % (ip_address)
#output = subprocess.check_output(cmd, shell=True)
cmd = '~/tek/utils/tek_afg_read/tek_afg_read -i %s -d \"ACQ:MOD?\"' % (ip_address)
output = subprocess.check_output(cmd, shell=True)
mode = str(output.split()[0])
mode = mode[2:len(mode)-1]
cmd = '~/tek/utils/tek_afg_read/tek_afg_read -i %s -d \"ACQ:NUMAV?\"' % (ip_address)
output = subprocess.check_output(cmd, shell=True)
nmav = str(output.split()[0])
nmav = int(nmav)
cmd = '~/tek/utils/tek_afg_read/tek_afg_read -i %s -d \"WFMO:XIN?\"' % (ip_address)
output = subprocess.check_output(cmd, shell=True)
xincr = output.split()[0]
xincr = float(xincr)
if mode=='AVE':
   xincr = xincr * int(nmav)
cmd = '~/tek/utils/tek_afg_read/tek_afg_read -i %s -d \"WFMO:XZE?\"' % (ip_address)
output = subprocess.check_output(cmd, shell=True)
xzero = output.split()[0]
xzero = float(xzero)
cmd = '~/tek/utils/tek_afg_read/tek_afg_read -i %s -d \"WFMO:YMU?\"' % (ip_address)
output = subprocess.check_output(cmd, shell=True)
volt = output.split()[0]
volt = float(volt)
cmd = '~/tek/utils/tek_afg_read/tek_afg_read -i %s -d \"WFMO:YZE?\"' % (ip_address)
output = subprocess.check_output(cmd, shell=True)
yzero = output.split()[0]
yzero = float(yzero)
cmd = '~/tek/utils/tek_afg_read/tek_afg_read -i %s -d \"WFMO:YOF?\"' % (ip_address)
output = subprocess.check_output(cmd, shell=True)
yoffset = output.split()[0]
yoffset = float(yoffset)
print(xincr, xzero)
print(volt, yzero, yoffset)

#cmd = '~/tek/utils/tek_afg_read/tek_afg_read -i %s -d \"WFMO?\"' % (ip_address)
#output = subprocess.check_output(cmd, shell=True)
#print(output)

first = True
with open(OUTPUTFILE, mode='w') as f:
   for iEvent in range(nEvent):
      if iEvent%100 == 0:
         print('Getting %d event' % iEvent)
      cmd = './tek/utils/tek_afg_read/tek_afg_read -i %s -d \"CURV?\"' % (ip_address)
      output = subprocess.check_output(cmd, shell=True)
      val_str = str(output.split()[0])
      val_str = val_str.split(',')
      if first:
         for i in range(0,len(val_str)-1):
            val = i * xincr + xzero
            f.write('{:.9g} '.format(val))
         f.write('\n')
         first = False
      for i in range(1,len(val_str)-1):
         val = (float(val_str[i]) - yoffset) * volt + yzero
         f.write(str(val) + ' ')
      f.write('\n')

print("Got %d event data!" % nEvent)

end = time.time()
print(end - start)

