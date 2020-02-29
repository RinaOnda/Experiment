#!/usr/bin/env python

import os, sys
import datetime

OUTPUTFILE = './example.txt'
FILENUMBER = -1
if len(sys.argv) == 2:
    OUTPUTFILE = sys.argv[1]
elif len(sys.argv) == 3:
    OUTPUTFILE = sys.argv[1]
    FILENUMBER = int(sys.argv[2])
else:
    print('Usage: ./example.py [OUTPUTFILE]')
    print('Usage: ./example.py [OUTPUTFILE] [FILENUMBER]')
    exit(1)

def main():
    today = datetime.date.today()

    file_name = OUTPUTFILE
    if FILENUMBER>=0:
        file_name = file_name.split('.')[0] + '%06d.'%FILENUMBER + file_name.split('.')[1]

    with open(file_name, mode='w') as f:
        f.write('Hello, world!\n')
        f.write('Today is %s'%today)

#--------------------------------------------------------------------
if __name__ == '__main__':
    main()
