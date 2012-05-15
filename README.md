Spark
=====
A quick port of [Zach Holman (@holman)'s awesome `spark` script](https://github.com/holman/spark) in Python, also usable as a function from Python rather than a command line utility only.

Usage
-----
From the command line (protip: use `./spark -h`):

```
user@box:~$ ./spark.py 1 2 3 4 5
 ▂▄▆█
user@box:~$ ./spark.py 23 5 12 42 13 6 3 4
▄ ▂█▂▁  
user@box:~$ ./spark.py --min 0 12 23 17 14 32 16 31
▃▆▄▄██
user@box:~$ echo 1 2 3 4 7 2 | ./spark.py
 ▁▃▄█▁
```

From python:

```python
from spark import spark
# simple spark with a tuple as data
sparks = spark((1,2,3,4,5))
# spark with a range iterable and custom ticks
sparks = spark(range(16), u' ░▒▓█')
# spark with a data list with a lower bound
sparks = spark([12, 14, 16, 14, 12], vrange = (0, None))
```

Credits
-------
- @holman for coming up with the idea in the first place.
- @matthijskooijman for suggesting spanning the output over multiple lines.

