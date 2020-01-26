#! /usr/bin/env python
#monitor current

import gpib, time, sys
from datetime import datetime

path = '.'
ncycle = 100000
nmeas = 10
interval = 60#secondo
microampere = 1.e6
index = 0

#connect to picoammeter
picoam = gpib.find("picoammeter")

#initialize
print('initialize picoammeter')
gpib.write(picoam, "*RST") #reset settings
gpib.write(picoam, "SYST:ZCH ON") #zero check
gpib.write(picoam, "RANGE 2e-2") #set current range. -0.021-0.021 A
gpib.write(picoam, "RANGE:AUTO OFF") #change current range manually
gpib.write(picoam, "INIT") #read value of zero correction
gpib.write(picoam, "SYST:ZCOR:ACQ") #acquire value of zero correction
gpib.write(picoam, "SYST:ZCOR ON") #zero correction
gpib.write(picoam, "SYST:ZCOR OFF")
gpib.write(picoam, "SYST:ZCH OFF")

#turn on HV
gpib.write(picoam, "SOUR:VOLT:RANG 500") #set voltage range. (only 10, 50, 500 V)
gpib.write(picoam, "SOUR:VOLT:ILIM 25") #set current limit. (only 25, 250, 2.5e-3, 25e-3 A)
gpib.write(picoam, "SOUR:VOLT:ILIM 2.5e-3") #set current limit. (only 25, 250, 2.5e-3, 25e-3 A)
gpib.write(picoam, "SOUR:VOLT 56.37") #set voltage, V
gpib.write(picoam, "SOUR:VOLT:STAT ON") #turn on

#monitor current
print('start monitoring!')
for icycle in range(ncycle):
   print('getting data: %d/%d' % (icycle, ncycle))
   vals = []
   timestamp = time.time()
   now = datetime.fromtimestamp(timestamp)

   for imeas in range(nmeas):
      gpib.write(picoam, "READ?")
      time.sleep(1)
      val = gpib.read(picoam, 100)
      val = val[0:val.find('A')]
      val = float(val) * microampere
      vals.append(str(val))

   filename = '%s/current%d_%04d_%02d_%02d.txt' % (path, index, now.year, now.month, now.day)
   with open(filename, mode='a') as f:
      f.write(str(timestamp))
      for imeas in range(nmeas):
         f.write(' ' + vals[imeas])
      f.write('\n')
   if icycle<ncycle-1:
      print('waiting %d second...' % interval)
      time.sleep(interval)
print('finished!')

#turn off HV
gpib.write(picoam, "SOUR:VOLT:STAT OFF")
gpib.write(picoam, "SOUR:VOLT 0")

#close connection
gpib.close(picoam)
