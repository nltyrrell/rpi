import subprocess
import sys

child = subprocess.Popen(command, shell=True, stderr=subprocess.PIPE)
while True:
	out = child.stderr.read(1)
	if out == '' and child.poll() != None:
		break
	if out != '':
		sys.stdout.write(out)
		sys.stdout.flush()
