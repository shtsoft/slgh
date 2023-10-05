""" Describe the package in one line ...

Describe the design of the package ...
"""


import sys


from slgh import main


rc = 1
try:
    main()
    rc = 0
except Exception as e:
    print('Error: %s' % e, file=sys.stderr)
sys.exit(rc)
