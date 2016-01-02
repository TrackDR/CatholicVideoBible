#!/bin/sh


#Usage ./removechpcomments.sh newfldr
#./removechpcomments.sh newchps

newfldr=$1

pushd $newfldr

rm -f *aa.txt
rm -f *aarm.txt
rm -f *.bak
rm -f *aarm.txt*

files=`find -name '*.txt'`

for x in $files
do
    echo $x
    name=`echo $x | sed 's/\.\///g' | cut -d"." -f1`
    echo $name
    awk -f ../convertmulti2single.awk ${name}.txt > ${name}aa.txt
    ../removecomments.sh ${name}aa.txt ${name}aarm.txt
    #mytst=`tail -2 ${name}aarm.txt | head -1 | grep ":"`
    #if [ -z "$mytst" ]
    #then
        #echo "empty"
        #numlines=`wc -l ${name}aarm.txt | cut -d" " -f1`
        #rmline1=$numlines
        #rmline2=`expr $numlines - 1`
        #echo "Removing lines ${rmline1},${rmline2} from ${name}aarm.txt"
        #sed -i.bak -e "${rmline2},${rmline1}d" ${name}aarm.txt
    #else
#       echo "not empty"
 #   fi

    #numlines=`wc -l ${name}aarm.txt | cut -d" " -f1`
    #lastverse=`grep -n ":" ${name}aarm.txt | tail -1 | cut -d":" -f1`
    #cutlinenum=`expr $lastverse + 1`
    #sed -i.bak -e "${cutlinenum},${numlines}d" ${name}aarm.txt

done

popd











popd
