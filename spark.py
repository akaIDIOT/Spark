# coding=UTF-8

from math import ceil, floor

__version__ = (0, 4, 1)
__version_string__ = '.'.join(map(str, __version__))

# taken from https://github.com/holman/spark
TICKS = u' ▁▂▃▄▅▆▇█'

def spark(data, ticks = TICKS, vrange = (None, None), lines = 1, span = None):
	"""
	Creates a unicode graph from a data series of numbers. Argument vrange
	specifies lower and upper bounds as a tuple (lower, upper), None for
	either indicates no bound. Argument lines specifies the number of lines
	the output should span. Be aware that this assumes ticks[0] to be 'empty
	space' and ticks[len(ticks) - 1] to be 'filled space'. Argument span makes
	the spark span that number of characters, regardless of the size of the
	input, inter/extrapolating the data points as needed.

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

	>>> # multiline mode should produce the correct result
	>>> spark((1,2,3,4,5), '0123', lines = 2)
	u'00023\n02333'
	"""

	# smile and wave, boys, smile and wave
	if not data:
		return u''
	if vrange[0] is not None and vrange[1] is not None and vrange[1] - vrange[0] <= 0.0:
		raise ValueError('erronous value range: {range}'.format(range = vrange))
	if lines <= 0:
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

	# update data if a span of different length is needed
	if span and span is not len(data):
		def split(interval):
			# FIXME: something is still rather buggy in here (span over double length will create regular spikes, for example)
			start, end = interval
			if int(start) is int(end):
				# value should be taken from a single data point
				return (end - start) * data[int(start)]
			else:
				# value spans an index boundary
				# take the right partition of the leftmost point to be used
				value = (1 - start % 1) * data[int(start)]
				# slice out the values that would be 'skipped' by this partition (possibly empty)
				skipped = data[int(ceil(start)):int(end)]
				# add its sum to the value
				value += sum(skipped)
				# add the left partition of the rightmost point to be used
				value += (end % 1) * data[min(int(end), len(data) - 1)]

				# return the average value over the interval
				return value / (end - start)

		# calculate the width (amount of data) of a single spanned point
		width = float(len(data)) / span
		# create a list of tuples (start, end) to partition the data with
		pieces = [(i * width, (i + 1) * width) for i in range(span)]
		# split up the data with the created pieces
		data = map(split, pieces)

	columns = []
	for point in data:
		# find the relative (range 0.0--1.0) value
		point = (point - low) / diff if diff else 1.0
		# calculate the number of 'empty lines'
		empty = int((1.0 - point) * lines)
		# calculate the number of 'full lines'
		full = int(point * lines)

		if empty + full == lines:
			# point was exactly between two lines, no more chars needed
			point = u''
		else:
			# calculate the index of the character that fits best
			#   modulate the data point by line_step to get the data that is not yet graphed
			#   divide this value by line_step to get the relative value
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

