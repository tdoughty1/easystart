#!/usr/bin/env python
# -*- coding: ascii -*-

"""
Module Docstring Here
"""

__author__ = 'W. Todd Doughty (w.todd.doughty@gmail.com)'
__copyright__ = 'Copyright (c) 2016 W. Todd Doughty'
__license__ = 'MIT'
__version__ = '0.0.0'

# ----------------------------------------------------------------------------
# Code starts here.
# ----------------------------------------------------------------------------

# Import standard modules
from argparse import ArgumentParser
from os.path import isfile
from os import system


# Testing routine
def test():
    """ Testing Docstring """
    pass


# Main routine
def main(args):
    """
    Run standard checkers on any python module

    Currently runs:
        - pep8
        - pyflakes
        - pylint
        - pychecker
    """

    if not isfile(args.name):
        return 1

    system('pep8 ' + args.name)
    system('pyflakes ' + args.name)
    system('pylint ' + args.name)
    system('pychecker ' + args.name)


# Make it executable
if __name__ == '__main__':

    # Initialize Parser
    parser = ArgumentParser()

    # Insert arguments here
    parser.add_argument('name', help='Name of function to check')

    # Link to parser
    args = parser.parse_args()
    main(args)
