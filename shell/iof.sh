#!/bin/sh

n=3
as=(0 1 10)
bs=(1 5 8)

filename='./shell/example.txt'
for ((i=0 ; i < n ; ++i))
do
   a=${as[$i]}
   b=${bs[$i]}

   tmp='./shell/example_A_B.txt'
   tmp=${tmp/A/${a}}
   tmp=${tmp/B/${b}}

   ./shell/calculate.sh ${a} ${b}  > $tmp
   grep "a + b" $tmp | cut -c 9- >> $filename

done
