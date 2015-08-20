#!/usr/bin/python

"""
Usage: make_playlist directory name
Generates a .txt file playlist with whatever is in the directory with the given name
the playlist is in the ~/playlist directory
"""

from itertools import ifilter
import os.path
import re
from sys import argv, exit, stdout


PATTERN = re.compile('\.(mp3|ogg|flac|m4a)$', re.I)

def find_files(path):
    """Return all matching files beneath the path."""
    for root, dirs, files in os.walk(os.path.abspath(path)):
        for fn in sorted(ifilter(PATTERN.search, files)):
            yield os.path.join(root, fn)

def create_playlist(filenames):
    """Create a simple playlist from filenames."""
    entry = (
        '%s\n'
        )
    for filename in filenames:
        yield entry % (filename)


# def writePLS(playlist):
    

if __name__ == '__main__':
    if len(argv) != 3:
        exit('Usage: %s <name of playlist> <path to music files> ' % os.path.basename(argv[0]))

    filenames = find_files(argv[2])
    outfile = open('/home/pi/playlists/'+argv[1],'a')
    map(outfile.write, create_playlist(filenames))
