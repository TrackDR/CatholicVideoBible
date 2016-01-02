BEGIN {
    FS="\n"
    RS=""
    ORS=""
}

{
    x=1
    while ( x < NF ) {
        print $x " "
        x++
    }
    print $NF "\r\n\r\n"
}

