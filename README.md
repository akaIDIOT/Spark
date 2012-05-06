Spark
=====
A quick port of [Zach Holman (@holman)'s awesome `spark` script](https://github.com/holman/spark) in Python.

Usage
-----
From the command line:

```
user@box:~$ ./spark.py 1 2 3 4 5
▁▃▅▆█
user@box:~$ ./spark.py 5 12 42 13 6
▁▂█▃▁
```

From python:

```python
from spark import spark
# simple spark with a tuple as data
sparks = spark((1,2,3,4,5))
# spark with a range iterable and custom ticks
spark(range(16), u' ░▒▓█')
```

