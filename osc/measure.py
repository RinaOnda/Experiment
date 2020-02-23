#!/usr/bin/env python

import os, sys, subprocess
import time

ip_address = 'ip address of your device'
OUTPUTFOLDER = './'
OUTPUTFILE = OUTPUTFOLDER + 'test.txt'

start = time.time()
if len(sys.argv) == 3:
    ch = sys.argv[1]
    nEvent = int(sys.argv[2])
elif len(sys.argv) == 4:
    ch = sys.argv[1]
    nEvent = int(sys.argv[2])
    OUTPUTFILE = sys.argv[3]
else:
    print('Usage: ./measure.py [ch] [nEvent]')
    print('Usage: ./measure.py [ch] [nEvent] [outputfile]')
    exit(1)

res = []
for iEvent in range(nEvent):
   if iEvent%100 == 0:
      print('Getting %d event' % iEvent)
   cmd = './tek/utils/tek_afg_read/tek_afg_read -i %s -d \"MEASU:MEAS%s:VAL?\"' % (ip_address, ch)
   output = subprocess.check_output(cmd, shell=True)
   val = str(output.split()[0])
   val = val[2:len(val)-1] 
   res.append(val)

print("Got %d event data!" % nEvent)
with open(OUTPUTFILE, mode='w') as f:
   for iEvent in range(nEvent):
      f.write(res[iEvent] + '\n')

print("Finished output")
end = time.time()
print(end - start)

