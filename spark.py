#!/usr/bin/env python
# coding=UTF-8

__version__ = (0, 2)
__version_string__ = '.'.join(map(str, __version__))

# taken from https://github.com/holman/spark
TICKS = u' ▁▂▃▄▅▆▇█'

def spark(data, ticks = TICKS):
	"""
	Creates a unicode graph from a data series of numbers.
	"""
	# smile and wave, boys, smile and wave
	if not data:
		return u''
	# find the absolute range
	low = min(data)
	# force it to a float to keep it from screwing with the division
	diff = float(max(data) - low)
	# create the spark string (calculate the index in ticks string from the relative difference from min/max)
	return u''.join(map(lambda point: ticks[int(round((point - low) / diff * (len(ticks) - 1)))], data))

if __name__ == '__main__':
	import sys, shlex
	# get arguments from command line
	data = sys.argv[1:]
	if not data and not sys.stdin.isatty():
		# read a line from stdin, treat is as arguments when we're being piped / redirected
		data = shlex.split(sys.stdin.readline())

	# print the spark
	print spark(map(float, data))

