#!/bin/sh
##
## txt2psf.sh
##
## Made by jer
## Login   <jer@localhost.localdomain>
##
## Started on  Tue May 15 11:12:22 2007 jer
## Last update Tue May 15 14:12:18 2007 jer
##

chapter=$1
#chapter="GenCh1a"

font=$2
#font="Times-Roman24"

#pr -d -t ${chapter}.txt | enscript -Eetext --escapes --no-header --word-wrap --font=$font -M Im640 -o ${chapter}${font}s640by480.ps

enscript --h-column-height=50 --no-header --word-wrap --font=$font -M Im640 ${chapter}.txt -o ${chapter}${font}s640by480.ps

gv ${chapter}${font}s640by480.ps &




enscript --landscape --no-header --word-wrap --font=Times-Roman24 18732-0.txt -o test.ps; rm test.pdf; ps2pdf test.ps
