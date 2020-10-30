F=$1 # this is the first argument and is my temperature in fehrenheit
C=$(( (F-32)*5/9 ))
echo "$F F = $C C"
