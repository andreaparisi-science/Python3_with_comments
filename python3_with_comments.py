# Multiline comments in python3
# Anything between #[  and #] will ignored

import sys
import subprocess

filename = ""
python_params = []
script_params = []
for arg in sys.argv:
	if arg[-24:] == "python3_with_comments.py":
		continue
	elif filename == "" and arg[0] == "-":
		python_params.append(arg)
	elif filename == "":
		filename = arg
	else:
		script_params.append(arg)

if filename != "":
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

	exec_cmd = ["python3"] + python_params + ["-"] + script_params
	subprocess.run(exec_cmd, 
			input=('\n'.join(lines)).encode('utf-8'))
else:
	subprocess.run("python3")

