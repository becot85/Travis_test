# Import the sys package to return exit codes
import sys

def try_exit(i=0):
    if i == 0:
        sys.exit(0)
    else:
        sys.exit(1)

print 'I got in!!'
try_exit(i=0)

