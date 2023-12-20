import argparse
import logging
import sys


from slgh import lib


CORE_VENV_DEPS = ('pip', 'setuptools')
logger = logging.getLogger(__name__)


def main():
    config = sys.argv[1]
    lib.run(config)
