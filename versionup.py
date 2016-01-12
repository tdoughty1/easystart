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


# Testing routine
def test():
    """ Testing Docstring """
    pass


# Main routine
def main(args):
    """ Main docstring """
    pass


# Make it executable
if __name__ == '__main__':

    # Initialize Parser
    parser = ArgumentParser()

    # Insert arguments here

    # Link to parser
    args = parser.parse_args()
    main(args)
