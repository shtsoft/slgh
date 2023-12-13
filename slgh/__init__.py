import argparse
import logging
import sys


from slgh import api.placeholder


CORE_VENV_DEPS = ('pip', 'setuptools')
logger = logging.getLogger(__name__)


def main(argv):
    config = argv[1]
    api.placeholder.run(config)
