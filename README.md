Spark
=====
A quick port of [Zach Holman (@holman)'s awesome `spark` script](https://github.com/holman/spark) in Python, also usable as a function from Python rather than a command line utility only.

Usage
-----
From the command line:

```
user@box:~$ ./spark.py 1 2 3 4 5
▁▃▅▆█
user@box:~$ ./spark.py 5 12 42 13 6
▁▂█▃▁
user@box:~$ echo 1 2 3 4 7 2 | ./spark.py
```

From python:

```python
from spark import spark
# simple spark with a tuple as data
sparks = spark((1,2,3,4,5))
# spark with a range iterable and custom ticks
sparks = spark(range(16), u' ░▒▓█')
```

