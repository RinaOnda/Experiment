#!/usr/bin/env python
#Submit job for sequence run numbers

import subprocess, time, os

runrange = [[1,2]]

user_name = 'name'
#set a limit to the number of your jobs
Njob_total = 160
Njob_limit = 100 
Njob_limit_left = 30

PBSFILE = 'example.pbs'
OUTPUTFILE = 'output.txt'

#skip if the run already exists
skip_exist_run = False

def main():

    subprocess.call('rm -vf Job.e*', shell=True)
    subprocess.call('rm -vf Job.o*', shell=True)

    for irange in range(len(runrange)):
        if (runrange[irange][1] < runrange[irange][0]):
            exit()

    for irange in range(len(runrange)):
        runstart = runrange[irange][0]
        runend = runrange[irange][1]
        print('_________________________________________________________')
        print('Start job submit of %d runs from %d to %d.'%(runend - runstart + 1, runstart, runend))

        for run in range(runstart, runend + 1, 1) :
            if skip_exist_run and check_file_exist(run):
                continue
            while 1 :
                Njob = subprocess.check_output('qstat | grep %s | wc -l '%user_name, shell=True)
                Njob_left = Njob_total - int(subprocess.check_output('qstat | wc -l ', shell=True))
                if (int(Njob) < Njob_limit and int(Njob_left)>Njob_limit_left):
                    break
                else :
                    print('Njob: %d. Wait.'%int(Njob))
                    time.sleep(10)

            print('Submit job : run %d'%run)
            subprocess.check_output('env OUTPUTFILE=%s FILENUMBER=%d qsub %s' %(OUTPUTFILE,run,PBSFILE), shell=True)
            time.sleep(0.3)

print('All Jobs are submitted.')

#______________________________________________________________________
def check_file_exist(run):
    file_name = OUTPUTFILE
    file_name = file_name.split('.')[0] + '%06d'%run + file_name.split('.')[1]
    if (os.path.exists(file_name)) :
        print('Skip run. File exist : '+ file_name)
        return True
    else :
        return False

#--------------------------------------------------------------------
if __name__ == '__main__':
    main()
