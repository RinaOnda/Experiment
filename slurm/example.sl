#!/bin/bash
###############################################################################
# A sample SLURM script to submit a job on 1 node
#
#  usage:
#        (0) Edit this script
#        (1) Submit the job.
#            % sbatch example.sl
#
###############################################################################

#SBATCH --partition=all
#SBATCH --ntasks=1
#SBATCH --job-name=Job
#SBATCH --output="Job-%j.out"
#SBATCH --error="Job-%j.err"

MY_HOST=`hostname`
MY_DATE=`date`

#
# Disable core dump. (Remove this line if you want to create core files)
#
ulimit -c 0

echo "Running on $MY_HOST at $MY_DATE"
echo "================================================================"

#
# Print envirionment
#
#echo "Running environment":
#env | sort
#echo "================================================================"

#
# Replace configuration file by yours
#

python example.py "$1" "$2"
#./example.exe "$1" "$2"

RET=$?
echo "Exit status: $RET"
echo "================================================================"
END_DATE=`date`
echo "End of run is $END_DATE"
