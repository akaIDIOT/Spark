#!/usr/bin/env python
# coding=UTF-8

__version__ = (0, 2, 1)
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

	# calculate the relative data values as 0.0 -- 1.0
	sparks = map(lambda point: (point - low) / diff, data)
	# calculate the relative data values as 0 -- index in ticks
	sparks = map(lambda value: int(round(value * (len(ticks) - 1))), sparks)
	# get the right character from ticks
	sparks = map(lambda index: ticks[index], sparks)

	# the above is equivalent to
	# map(lambda point: ticks[int(round((point - low) / diff * (len(ticks) - 1)))], data)

	return u''.join(sparks)

if __name__ == '__main__':
	import sys, shlex
	# get arguments from command line
	data = sys.argv[1:]
	if not data and not sys.stdin.isatty():
		# read a line from stdin, treat is as arguments when we're being piped / redirected
		data = shlex.split(sys.stdin.readline())

	# print the spark
	print spark(map(float, data))

