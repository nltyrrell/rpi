#!/usr/bin/python
"""
Usage: popularity.py
Prints out a list of playlist by number of plays
Created on 8 August 2015 - nt
"""

import numpy as np
import operator

log_in = open('/home/pi/scripts/logfile.txt','r')
logs = log_in.readlines()
logs = [i.strip() for i in logs]
log_in.close()

logdict = {}
logtup = ()
for i in logs:
    logdict[i] = logs.count(i)

lsort = sorted(logdict.items(),key=operator.itemgetter(1),reverse=True)
# print(lsort)

plonly = [i[0] for i in lsort]
nonly = [i[1] for i in lsort]

print("# of plays : Playlist")
for n,i in enumerate(plonly):
    print(str(nonly[n])+' : '+i)

#     print(i)
