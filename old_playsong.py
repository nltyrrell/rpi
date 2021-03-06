#!/usr/bin/python

from Adafruit_CharLCD import Adafruit_CharLCD
from subprocess import *
from time import sleep, strftime
from datetime import datetime
import numpy as np
import os
import sys


if len(sys.argv) != 2:
	sys.exit('Usage: %s <name of playlist>' % os.path.basename(sys.argv[0]))

lcd = Adafruit_CharLCD()
lcd.begin(16, 1)

in_plist = '/home/pi/playlists/%s.txt' %sys.argv[1]

cmd = 'mplayer -identify -quiet -playlist %s' %in_plist
p = Popen(cmd, shell=True, stderr=PIPE, stdout=PIPE)
song = ''
artist='artist'
track='track'
print("MPLAYER CONTROLS:\n q  quit \n </>  skip forwards/back \n 9/0  Volume Up/Down \n space or p  Pause") 

while True:
    out = p.stdout.readline() #(1)
    if out == '' and p.poll() != None:
        lcd.clear()
        break
    if out.startswith('Playing'):
        song = out[8:-2]
        print("Song info: %s"%song)
        info_cmd = ["mediainfo",song]
        medinfo = Popen(info_cmd, stdout=PIPE)
        for line in medinfo.stdout.readlines():
            if line.startswith('Performer'):
                artist = line.split(':', 1)[1].strip()
            if line.startswith('Track name '):
                track = line.split(':', 1)[1].strip()
        print("artist %s"%artist)
        print("track %s"%track)
        lcd.clear()
        lcd.message('%s \n'%artist)
        lcd.message('%s '%track)
        maxlen = max(len(artist),len(track))
        if maxlen>16:
            s=0
            while s<(maxlen-16):
                lcd.scrollDisplayLeft()
                sleep(0.2)
                s += 1
            sleep(3)
            s=0
            while s<(maxlen-16):
                lcd.scrollDisplayRight()
                sleep(0.2)
                s += 1

    if out != '':
# 		sys.stdout.write(out)
		sys.stdout.flush()

