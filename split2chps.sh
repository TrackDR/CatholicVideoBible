#/bin/sh

# Usage ./split2chps.sh 8300.txt newfldrname
# ./split2chps.sh 8300.txt newchps

infile=$1

newfldr=$2


rm -rf $newfldr
mkdir -p $newfldr

grep -n Chapter $infile | cut -d":" -f1 > numlista.tmp
cp numlista.tmp numlist.tmp
badline1=`grep -n 57401 numlist.tmp | cut -d":" -f1`
badline2=`grep -n 57883 numlist.tmp | cut -d":" -f1`
echo "Removing lines $badline1 $badline2"
sed -i.bak -e "${badline2}d" numlist.tmp
sed -i.bak -e "${badline1}d" numlist.tmp

numlines=`wc -l numlist.tmp | cut -d" " -f1`

echo "Numlines: $numlines"

x=1

endx=`expr $numlines - 1`


while [ $x -le $endx ]
do
    echo $x
    y=`expr $x + 1`
    currnum=`head -$x numlist.tmp | tail -1`
    nextnum=`head -$y numlist.tmp | tail -1`
    chplen=`expr $nextnum - $currnum`
    echo "$currnum $nextnum $chplen"

    myfilename=`head -$currnum $infile | tail -1`
    mytstC=`echo $myfilename | grep "Canticle"`
    mytstK=`echo $myfilename | cut -d" " -f1`

    if [ ! -z "$mytstC" ]
    then
        filename=`echo "$myfilename" | cut -d" " -f1,2,3,5 | tr -d '\n' | tr -d '\r' | sed 's/ /_/g'`
    elif [ ! -z "${mytstK##*[!0-9]*}" ]
        then
        filename=`echo "$myfilename" | cut -d" " -f1,2,4 | tr -d '\n' | tr -d '\r' | sed 's/ /_/g'`
    else
        filename=`echo "$myfilename" | cut -d" " -f1,3 | tr -d '\n' | tr -d '\r' | sed 's/ /_/g'`
    fi

    filename=`echo $filename | tr -d '.'`

    echo $filename
    #filename="${filename}.txt"
    echo "Creating $filename"
    nextnum=`expr $nextnum - 1`
    head -$nextnum $infile | tail -$chplen > $newfldr/$filename.txt

    x=`expr $x + 1`
done
