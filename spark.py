#!/usr/bin/env python
# coding=UTF-8

__version__ = (0, 3)
__version_string__ = '.'.join(map(str, __version__))

# taken from https://github.com/holman/spark
TICKS = u' ▁▂▃▄▅▆▇█'

def spark(data, ticks = TICKS, vrange = (None, None), lines = 1):
	"""
	Creates a unicode graph from a data series of numbers. Argument vrange 
	specifies lower and upper bounds as a tuple (lower, upper), None for 
	either indicates no bound. Argument lines specifies the number of lines 
	the output should span. Be aware that this assumes ticks[0] to be 'empty
	space' and ticks[len(ticks) - 1] to be 'filled space'.

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

	>>> # lower and upper bounds should be respected
	>>> spark((-3, -2, -1, 0, 1, 2, 3, 4, 5), '0123', (0, 3))
	u'000012333'
	"""
	# smile and wave, boys, smile and wave
	if not data:
		return u''
	if vrange[0] is not None and vrange[1] is not None and vrange[1] - vrange[0] <= 0.0:
		raise ValueError('erronous value range: {range}'.format(range = vrange))
	if lines < 0:
		raise ValueError('cannot format to zero or less lines')

	# find the absolute range
	low = min(data)
	# if a lower bound is specified, set low and fix data accordingly
	if vrange[0] is not None:
		low = vrange[0]
		# make sure no value is below lower bound
		data = map(lambda point: max(point, low), data)

	# find the difference (force to float for divisions later)
	diff = float(max(data) - low)
	if vrange[1] is not None:
		diff = float(vrange[1] - low)
		# make sure no value is over upper bound
		data = map(lambda point: min(point, low + diff), data)

	# calculate the amount of data a single line would occupy
	line_step = diff / lines

	columns = []
	for point in data:
		# find the relative (range 0.0--1.0) value
		point = (point - low) / diff
		# calculate the number of 'empty lines'
		empty = int((1.0 - point) * lines)
		# calculate the number of 'full lines'
		full = int(point * lines)

		if empty + full == lines:
			# point was exactly between two lines, no more chars needed
			point = u''
		else:
			# calculate the index of the character that fits best
			#	modulate the data point by line_step to get the data that is not yet graphed
			#	divide this value by line_step to get the relative value
			#   multiply this by the length of the ticks string and round this to get the correct index
			point = int(round((point * diff) % line_step / line_step * (len(ticks) - 1)))
			point = ticks[point]
		
		# append the 'column' to the list
		columns.append(ticks[0] * empty + point + ticks[len(ticks) - 1] * full)

	# 'transpose' the 'matrix' to get lines rather than columns
	sparks = []
	for line in range(lines):
		sparks.append(u''.join(column[line] for column in columns))
	
	# join the lines on a newline to get the final value
	return u'\n'.join(sparks)

if __name__ == '__main__':
	import argparse, shlex, sys

	# create an argument parser for command line arguments
	parser = argparse.ArgumentParser(description = 'Graph numerical data as an ascii graph')
	parser.add_argument('--min', default = None, type = float, help = 'lower value bound', dest = 'min')
	parser.add_argument('--max', default = None, type = float, help = 'upper value bound', dest = 'max')
	parser.add_argument('--lines', default = 1, type = int, help = 'the number of lines to format the spark to', dest = 'lines')
	parser.add_argument('data', nargs = '*', type = float, help = 'data to graph', metavar = 'VALUE')
	# collect arguments in args
	args = parser.parse_args()

	# override args.data if no data specified
	if not args.data and not sys.stdin.isatty():
		# read a line from stdin, treat is as arguments when we're being piped / redirected
		args.data = shlex.split(sys.stdin.readline())

	# print the spark
	print spark(map(float, args.data), vrange = (args.min, args.max), lines = args.lines)

