#!/usr/bin/python

from Adafruit_CharLCD import Adafruit_CharLCD
from subprocess import *
from time import sleep, strftime
from datetime import datetime
import numpy as np
import os
import sys

statdict = {'TripleR':'http://freezone.iinet.net.au/include/radio/playlists/triple-r-fm.m3u',
            'PBS1067':'http://eno.emit.com:8000/pbsfm_live_64.mp3.m3u',
            'ABC774':'http://www.abc.net.au/res/streaming/audio/aac/local_melbourne.pls',
            'Double J':'http://abc.net.au/res/streaming/audio/aac/dig_music.pls',
            'Grandstand':'http://abc.net.au/res/streaming/audio/aac/grandstand.pls',
            'Radio National':'http://abc.net.au/res/streaming/audio/aac/news_radio.pls'}

if len(sys.argv) != 2:
	sys.exit('Usage: %s <name of station> \n List of stations \n %s' % (os.path.basename(sys.argv[0]), statdict.keys()))

lcd = Adafruit_CharLCD()
lcd.begin(16, 1)

in_station = statdict[str(sys.argv[1])]
cmd = 'mplayer -identify -quiet -playlist %s' %in_station

# cmd = 'mplayer -quiet -identify -playlist http://freezone.iinet.net.au/include/radio/playlists/triple-r-fm.m3u'
p = Popen(cmd, shell=True, stderr=PIPE, stdout=PIPE)
song = ''
station='station'
website='website'
print("MPLAYER CONTROLS:\n \
        Skip Forwards/Back    </>  \n \
        Volume Up/Down        9/0  \n \
        Pause                 space or p \n   \
        Quit                  q ") 

while True:
    out = p.stdout.readline() #(1)
    if out == '' and p.poll() != None:
        lcd.clear()
        break
    if out.startswith('Name'):
#         station = out[8:-2]
        station = out.split(':', 1)[1].strip()
        print("station: %s"%station)
        lcd.clear()
        lcd.message('%s '%station)

        if len(station)>16:
            s=0
            while s<(len(station)-16):
                lcd.scrollDisplayLeft()
                sleep(0.2)
                s += 1
            sleep(3)
            s=0
            while s<(len(station)-16):
                lcd.scrollDisplayRight()
                sleep(0.2)
                s += 1

    if out != '':
#         sys.stdout.write(out)
        sys.stdout.flush()

