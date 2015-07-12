#!/usr/bin/python

from Adafruit_CharLCD import Adafruit_CharLCD
from subprocess import *
from time import sleep, strftime
from datetime import datetime
import numpy as np
import sys

lcd = Adafruit_CharLCD()

in_plist = sys.argv[0]

lcd.begin(16, 1)

def readplaylist(filestr):
	fileobj = open(filestr, 'r')
	outputstr = fileobj.readlines()
	fileobj.close()
	textarray = np.array([[float(n) for n in line.split()] for line in outputstr])
	return textarray

def run_cmd(cmd):
    p = Popen(cmd, shell=True, stdout=PIPE)
    output = p.communicate()[0]
    return output

plist = readplaylist(in_plist)

for song in plist:
	track = "mediainfo "+song
	music = "mplayer -quiet "+song

lcd.clear()
songname = run_cmd(cmd)
lcd.message(songname)
lcd.message('IP %s' % (ipaddr))

#p= subprocess.Popen(['mplayer', url], stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
#for line in p.stdout:
#    if line.startswith('ICY Info:'):
#        info = line.split(':', 1)[1].strip()
#        attrs = dict(re.findall("(\w+)='([^']*)'", info))
#        print 'Stream title: '+attrs.get('StreamTitle', '(none)')
#    sleep(2)
#while 1:
#    lcd.clear()
#    ipaddr = run_cmd(cmd)
#    lcd.message(datetime.now().strftime('%b %d  %H:%M:%S\n'))
#    lcd.message('IP %s' % (ipaddr))
#    sleep(2)
