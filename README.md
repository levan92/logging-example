# Logging Example

Template for Python Logging

`main.py`

```python3
import logging 

format = "[%(asctime)s] [%(levelname)s] [%(name)s] %(message)s"

# set up logging to file
logging.basicConfig(filename=args.logfile, level=args.loglevel, format=format)

# set up logging to console
console = logging.StreamHandler()
console.setLevel(args.loglevel)
formatter = logging.Formatter(format)
console.setFormatter(formatter)
logging.getLogger('').addHandler(console)
logger = logging.getLogger('logging_example')
```

Other files

```python3
import logging
logger = logging.getLogger(__name__)
```

## P.S.

`deep_sort_realtime` is a python package, included in this example to illustrate that logger config is carried over to logging in python packages.

`pip install deep-sort-realtime` if you want to try it too. 
