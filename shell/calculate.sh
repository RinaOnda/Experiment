#!/bin/sh

a="$1"
b="$2"

eq="a + b = answer"
ans="$(echo "$a + $b"|bc)"
echo ${eq/answer/${ans}}

eq="a - b = answer"
ans="$(echo "$a - $b"|bc)"
echo ${eq/answer/${ans}}

eq="a x b = answer"
ans="$(echo "$a * $b"|bc)"
echo ${eq/answer/${ans}}

eq="a / b = answer"
ans="$(echo "$a / $b"|bc)"
echo ${eq/answer/${ans}}

eq="a / b = answer"
ans="$(echo "scale=3; $a / $b"|bc)"
echo ${eq/answer/${ans}}

if test "$(echo "$a > $b"|bc)" -eq 1;then
   echo "a>b"
elif test "$(echo "$a < $b"|bc)" -eq 1;then
   echo "a<b"
else
   echo "a=b"
fi

eq="[a] = answer"
ans="$(echo ${a} | sed s/\.[0-9,]*$//g)"
if test "$(echo "$a < 0"|bc)" -eq 1;then
   ans="$(echo "$ans - 1"|bc)"
elif test "$(echo "$a == 0"|bc)" -eq 1;then
   ans=0
fi
echo ${eq/answer/${ans}}
