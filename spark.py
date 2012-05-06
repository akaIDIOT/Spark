#!/usr/bin/env python
# coding=UTF-8

# taken from https://github.com/holman/spark
TICKS = u'▁▂▃▄▅▆▇█' # TODO: add a space (0) in front?

def spark(data, ticks = TICKS):
	"""
	Creates a unicode graph from a data series of numbers.
	"""
	# find the absolute range
	low = min(data)
	# force it to a float to keep it from screwing with the division
	diff = float(max(data) - low)
	# create the spark string (calculate the index in ticks string from the relative difference from min/max)
	return u''.join(map(lambda point: ticks[int(round((point - low) / diff * (len(ticks) - 1)))], data))

if __name__ == '__main__':
	# print a spark from the command line arguments
	import sys
	data = map(float, sys.argv[1:])
	print spark(data)

