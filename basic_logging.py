"""
This script demonstrates the basics of logging in Python.
"""

# Import logging package
import logging

# Grab the current logging instance and assign it to 'log'.
log = logging.getLogger('MyLog')

# Some secret sauce that we'll come back to later...
handler = logging.StreamHandler()
formatter = logging.Formatter('%(levelname)s: %(message)s')
handler.setFormatter(formatter)
log.addHandler(handler)

# Log something.
log.error('We just logged an error!')

"""
There are 5 levels of logging that can be called. What do you expect to 
see and what do you see? 

What happened to the debug and info messages? By 
default the logging level is set to '"'warning'. We can set the logging level 
to whatever we want. Uncomment the first line below and experiment to see 
what happens as you change logging level.
"""
# log.setLevel(logging.DEBUG)
log.critical('This is a critical message')
log.error('This is an error message')
log.warning('This is a warning message')
log.info('This is an info message')
log.debug('This is a debug message')

