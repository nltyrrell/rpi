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

in_plist = '/home/pi/playlists/%s' %sys.argv[1]

len_plist = open(in_plist,'r')
playtime = []
hourtime = []
mintime = []
sectime = []
for n,i  in enumerate(len_plist.readlines()):
    print('n = %s'%n)
    print i
    info_cmd = ["mediainfo",i.strip()]
    medinfo = Popen(info_cmd, stdout=PIPE)
    for line in medinfo.stdout.readlines():
        if line.startswith('Duration'):
            dur = line.split(':', 1)[1].strip()
            if dur.find('h')>0:
                hdur = dur.split('h',1)[0]
                mdur = dur.split('h',1)[1][0:-2]
                sdur = 0
            else:
                hdur = 0
                sdur = dur.split('mn', 1)[1][0:-1]
                mdur = dur.split('mn', 1)[0]
    print(dur)
    print('hour %s' %hdur)
    print('min %s' %mdur)
    print('sec %s' %sdur)
    playtime.append(dur)
    hourtime.append(hdur)
    mintime.append(mdur)
    sectime.append(sdur)
har = np.array(hourtime).astype('float')
mar = np.array(mintime).astype('float')
sar = np.array(sectime).astype('float')

print('\n')
hours = har.sum()
print('H %s' %hours)
hours = hours + np.floor(mar.sum()/60)
print('H %s' %hours)
minutes = np.mod(mar.sum(),60)
print('M %s' %minutes)
minutes = minutes + np.round(sar.sum()/60)
print('M %s' %minutes)
if minutes>59:
    hours += 1
    minutes = np.mod(minutes,60)
print('\n')
print('Total playlist time: '+str(hours)[0:-2]+'h '+str(minutes)[0:-2]+'m')


# plist_len = len(len_plist.readlines())
len_plist.close()

