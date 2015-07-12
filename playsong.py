#!/usr/bin/python

from Adafruit_CharLCD import Adafruit_CharLCD
from subprocess import *
from time import sleep, strftime
from datetime import datetime
import numpy as np
import os
import sys


# def writePLS(playlist):
    

if len(sys.argv) != 2:
	sys.exit('Usage: %s <name of playlist>' % os.path.basename(sys.argv[0]))

lcd = Adafruit_CharLCD()

in_plist = '/home/pi/playlists/%s.txt' %sys.argv[1]

lcd.begin(16, 1)

def readplaylist(filestr):
	with open(filestr) as f:
		outstr = f.read().splitlines()
# 	textarray = np.array([[str(n) for n in line.split()] for line in outputstr])
	return outstr #textarray

def run_cmd(cmd):
    p = Popen(cmd, shell=True, stdout=PIPE)
    output = p.communicate()[0]
    return output


cmd = 'mplayer -identify -quiet -playlist %s' %in_plist
p = Popen(cmd, shell=True, stderr=PIPE, stdout=PIPE)
song = ''
artist='artist'
track='track'

while True:
	out = p.stdout.readline() #(1)
	if out == '' and p.poll() != None:
		lcd.clear()
		break
	if out.startswith('Playing'):
		song = out[8:-2]
		print("Song info: %s"%song)
		print "LAUNCH MEDIATHINGY"
		info_cmd = ["mediainfo",song]
		minfo = Popen(info_cmd, stderr=PIPE, stdout=PIPE)
		for line in minfo.stdout.readlines():
			if line.startswith('Performer'):
				artist = line.split(':', 1)[1].strip()
			if line.startswith('Track name '):
				track = line.split(':', 1)[1].strip()
		print("artist %s"%artist)
		print("track %s"%track)

# 		break
	if out != '':
# 		sys.stdout.write(out)
		sys.stdout.flush()

	lcd.clear()
	lcd.message('%s \n'%artist)
	lcd.message('%s '%track)
	if len(artist)>16 or len(track)>16:
		s=0
		while s<(len(artist)-16):
			lcd.DisplayLeft()
			sleep(0.4)
			s=s+1
		sleep(3)
# songname = run_cmd(cmd)
# lcd.message(songname)
# lcd.message('IP %s' % (ipaddr))

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
