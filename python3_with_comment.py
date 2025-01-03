# Multiline comments in python3
# Anything between #[  and #] will ignored

import sys
import subprocess

filename = sys.argv[-1]
params = sys.argv[1:-1]
with open(filename) as ffin:
	lines = ffin.readlines()

incomment = False
for idx in range(len(lines)):
	line = lines[idx]
	if not incomment:
		pos = line.find("#[")
		if pos >= 0:
			lines[idx] = line[0:pos]
			incomment = True

	if incomment:
		pos = line.find("#]")
		if pos >= 0:
			lines[idx] = line[pos+2:]
			incomment = False
		else:
			lines[idx] = ""

exec_cmd = ["python3"] + params
subprocess.run(exec_cmd, 
		input=('\n'.join(lines)).encode('utf-8'))

