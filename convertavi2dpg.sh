#!/bin/sh
##
## convertavi2dpg.sh
##
## Made by jer
## Login   <jer@localhost.localdomain>
##
## Started on  Fri May 25 20:06:33 2007 jer
## Last update Fri May 25 21:17:41 2007 jer
##

inmovie=$1
#  my.dpg
outmovie=$2
fps=$3

samples=22050
numframes=6310

#Method
#You will need Mplayer, mencoder, sox, cat and a hex editor.
#The first step is to create a plain mpg1 video file. I did this using :
#Code:
#mencoder foo.avi  -o foo.mpg -ovc lavc -lavcopts vcodec=mpeg1video:vbitrate=160000 -nosound -ofps 25 -vf scale=256:192
mencoder $inmovie  -o tmp.mpg -ovc lavc -lavcopts vcodec=mpeg1video:vbitrate=160000 -nosound -ofps ${fps} -vf scale=256:192

#This creates an mpeg1 (named foo.mpg) file with a bitrate of 160000 bps and resolution of 256 x 192 (a little high for the DS i think).
#Now we create a pcm (wav) file from the avi.
#Code:
mplayer $inmovie -dumpaudio -dumpfile output.dmp
mplayer output.dmp -ao pcm:file=output.wav

#This wav will have the same sample rate and bitrate of the original file.
#Now we convert the wav into the format expected by moonshell (WAV or wav49 or WAV GSM 6.01 call it what you want). I did this by
#Code:
sox output.wav -r $samples -g -c 1 output.gsm.wav

#Replace 44100 with the sample rate of your audio file.
#You can check this is the correct format by running
#Code:
#mplayer output.gsm.wav


audiosize=`wc -c output.gsm.wav | cut -d" " -f 1`
videosize=`wc -c tmp.mpg | cut -d" " -f 1`

#numframes=`cat tmp.mpg | grep frames | grep -v Flushing | cut -d" " -f 17`


#./headermaker <#frames> <fps> <samples> <audiosize> <videosize> <filename>
./headermaker $numframes $fps $samples $audiosize $videosize 36byteheader

#The codec should read "Selected audio codec: [msgsm] afm:msgsm (MS GSM)" if correct.
#Now create a file which is 36 bytes long. This forms you header, which i'll talk about in a minute. Now to create you movie file you do
#Code:
cat 36byteheader output.gsm.wav tmp.mpg > $outmovie

audiosize=1130670
videosize=615788

#DPG0   (4 bytes)              | 44 50 47 30

#frames (2 bytes)   (6310)     | 18 A6 or? A6 18
#spacing(2 bytes)              | 00 00

#fps    (2 bytes)   (25)       | 00 19 or? 19 00
#spacing(2 bytes)              | 00 00

#audio srate (22050) (2 bytes) | 56 22 or? 22 56
#spacing(2 bytes)              | 00 00

#num audio channels  (2 bytes) | 00 01 or? 01 00
#spacing(2 bytes)              | 00 00

#start of wav file-36(2 bytes) | 00 24 or? 24 00
#spacing(2 bytes)              | 00 00

#end of wav file (4 bytes)     |

#start of video file (4 bytes) |

#end of video file (4 bytes)   |
