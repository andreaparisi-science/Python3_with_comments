# Python3 multiline comments

This is a simple preprocessing script that will invoke the python3 interpreter on a 
user provided script, where code enclosed within multiline comments has been removed.

Start of multiline comment: #[  

End of multiline comment: #]  

It will allow the script to be run normally even when directly using the standard python interpreter



## Example

The following code has a set of dictionary entries.  We wish to comment out some of them
because we are testing and developing, and we just want to hide part of the code.

	#!/bin/python3

	dataset = {
		"set 1": {
			"option 1": "This is option 1",
			"option 2": "This is option 2",
		},
		"set 2": {
			"option 1": "This is option 1",
			"option 2": "This is option 2",
			"option 3": "This is option 3",
		},
		"set 3": {
			"option 1": "This is option 1",
			"option 2": "This is option 2",
			"option 3": "This is option 3",
		}
	}



We cannot achieve this effect using an if statement, nor with a multiline comment.  We can instead use:

	#!/bin/python3

	dataset = {
	#[
		"set 1": {
			"option 1": "This is option 1",
			"option 2": "This is option 2",
		},
	#]
		"set 2": {
			"option 1": "This is option 1",
			"option 2": "This is option 2",
			"option 3": "This is option 3",
		} #,
	#[
		"set 3": {
			"option 1": "This is option 1",
			"option 2": "This is option 2",
			"option 3": "This is option 3",
		}
	#]
	}


This will only leave the second entry, where the last comma has been commented out.


## Usage 

To use this script under linux, place it somewhere (for instance the bin directory)
and set an alias in your ~/.bashrc file (or equivalent according to the shell you are using)

For example:

	alias python3="$HOME/bin/python3_with_comments"

Then reload the aliases:

	source ~/.bashrc

And you should be done.


If you are using Windows, I am not sure what you should do as I assume you are not using a command line to run python scripts.  If you are using the command line, then you should know what to do.  If you do not, well... good luck... I do not use Windows for development with python.  If you find out and want to help other users, please let me know so that I can add instructions here.


