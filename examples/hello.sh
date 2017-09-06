#!/bin/bash
echo "Hello world!"

a=5
b=7
echo "a = $a and b = $b"

c=$((a+$b))
echo c = $c

echo There are $# arguments
echo These are the arguments: $*
echo This is the first arg $1

echo This is the 12th arg $0

if ((a<b))
then 
   echo "do something"
elif test $c -lt $b
then
   echo "do something else"
else
   echo "do whatever"
fi
# put a comment
count=1
while ((count<5))
do
    echo $count
    count=$((count+1))
done

echo
echo

for i in $*
do
    echo $i
done
echo
echo

for ((i=0; i<5; i++))
do
    echo "i = $i, val of arg = ${!i}"
done
