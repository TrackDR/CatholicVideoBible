#!/bin/sh

# ./removecomments.sh 8300aa.txt 8300aarm.txt

infile=$1

outfile=$2

echo "Calculating and putting into $outfile.2.txt"
#grep -n '^[0-9]' $infile | cut -d":" -f1 > $outfile.2.txt
#grep -n ":" $infile | cut -d":" -f1 > $outfile.2.txt
# Look at field 2 and if it's a number then print field 1-the line num
grep -n ":" $infile | awk -F: '{if ($2 ~ /^[0-9]+$/) print $1 }' > $outfile.2.txt

numlines=`wc -l $outfile.2.txt | cut -d" " -f1`
echo "Numlines: $numlines"



cp $infile $outfile

x=`expr $numlines - 1`

while [ $x -ge 1 ]
do
    echo $x
    y=`expr $x + 1`
    currnum=`head -$x $outfile.2.txt | tail -1`
    nextnum=`head -$y $outfile.2.txt | tail -1`
    z=`expr $nextnum - $currnum`
    if [ $z -gt 2 ]
    then
        delnum1=`expr $currnum + 1`
        delnum2=`expr $nextnum - 2`
        sed -i.bak -e "${delnum1},${delnum2}d" $outfile
        echo "$x deleted $delnum1 $delnum2 from $outfile"
    fi

    x=`expr $x - 1`
done

numlines=`wc -l $outfile | cut -d" " -f1`
#lastverse=`grep -n ":" $outfile | tail -1 | cut -d":" -f1`
lastverse=`grep -n ":" $outfile | awk -F: '{if ($2 ~ /^[0-9]+$/) print $1 }' | tail -1`
cutlinenum=`expr $lastverse + 1`
echo "Deleting ${cutlinenum},${numlines} from $outfile"
sed -i.bak -e "${cutlinenum},${numlines}d" $outfile


rm $outfile.2.txt
