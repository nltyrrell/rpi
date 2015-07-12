#!/usr/bin/python

"""
Usage: gen_playlist directory name
Generates a .PLS file playlist with whatever is in the directory with the given name

"""

from itertools import ifilter
import os.path
import re
from sys import argv, exit, stdout


PATTERN = re.compile('\.(mp3|ogg|flac)$', re.I)

def find_files(path):
    """Return all matching files beneath the path."""
    for root, dirs, files in os.walk(os.path.abspath(path)):
        for fn in sorted(ifilter(PATTERN.search, files)):
            yield os.path.join(root, fn)

def create_playlist(filenames):
    """Create a PLS playlist from filenames."""
    yield '[playlist]\n\n'
    num = 0

    entry = (
        'File%d=%s\n'
        'Title%d=%s\n'
        'Length%d=-1\n\n')
    for filename in filenames:
        num += 1
        title = os.path.splitext(os.path.basename(filename))[0]
        yield entry % (num, filename, num, title, num)

    yield (
        'NumberOfEntries=%d\n'
        'Version=2\n') % num

# def writePLS(playlist):
    

if __name__ == '__main__':
    if len(argv) != 3:
        exit('Usage: %s <path to music files> <name of playlist>' % os.path.basename(argv[0]))

    filenames = find_files(argv[1])
    outfile = open('/home/pi/playlists/'+argv[2]+'.pls','w')
    map(outfile.write, create_playlist(filenames))
