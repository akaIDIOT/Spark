#!/usr/bin/env python
# coding=UTF-8

__version__ = (0, 2, 2)
__version_string__ = '.'.join(map(str, __version__))

# taken from https://github.com/holman/spark
TICKS = u' ▁▂▃▄▅▆▇█'

def spark(data, ticks = TICKS):
	"""
	Creates a unicode graph from a data series of numbers.

	>>> # range of length ticks should be equal to ticks string
	>>> ticks = u'0123456789'
	>>> spark(range(len(ticks)), ticks)
	u'0123456789'

	>>> # no data should result in empty sparks string
	>>> spark('')
	u''

	>>> # numbers should be rounded correctly
	>>> spark((1, 2, 4, 5, 9), '01')
	u'00011'
	"""
	# smile and wave, boys, smile and wave
	if not data:
		return u''
	# find the absolute range
	low = min(data)
	# force it to a float to keep it from screwing with the division
	diff = float(max(data) - low)

	sparks = []
	for point in data:
		# find the relative (range 0.0--1.0) value
		point = (point - low) / diff
		# turn relative value into rounded absolute value (range 0--len(ticks)-1)
		point = int(round(point * (len(ticks) - 1)))
		# append the tick character to the list
		sparks.append(ticks[point])

	# the above is equivalent to
	# map(lambda point: ticks[int(round((point - low) / diff * (len(ticks) - 1)))], data)

	# join the sparks into a single string
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

