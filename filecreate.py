#!/usr/bin/env python
# -*- coding: ascii -*-

"""
Module with function to automatically create new module files with appropriate
metadata from Easy Start configuration
Docstrings: http://www.python.org/dev/peps/pep-0257/
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


# Testing routine
def test():
    """ Testing Docstring """
    pass


# Main routine
def main(args):

    # Ensure it's a .py module
    if '.py' not in args.name:
        name = args.name + '.py'
    else:
        name = args.name

    # Open python module writer
    f = open(name, 'w')

    # Write heading encoding
    f.write('#!/usr/bin/env python\n')
    f.write('# -*- coding: ascii -*-\n\n')
    
    # Write module docstring placeholder
    f.write('"""\nModule Docstring Here\n"""\n\n')

    # Write module metadata
    # TODO Implement reading config file
    f.write("__author__ = 'W. Todd Doughty (w.todd.doughty@gmail.com)'\n")
    f.write("__copyright__ = 'Copyright (c) 2016 W. Todd Doughty'\n")
    f.write("__license__ = 'MIT'\n")
    f.write("__version__ = '0.0.0'\n\n")

    # Write code divider
    f.write('# ' + '-'*76 + '\n')
    f.write('# Code starts here.\n')
    f.write('# ' + '-'*76 + '\n\n')

    # Write import (any command line function should use argparse)
    f.write('# Import standard modules\n')
    f.write('from argparse import ArgumentParser\n\n\n')

    # Write testing module placeholder
    f.write('# Testing routine\n')
    f.write('def test():\n')
    f.write('    """ Testing Docstring """\n')
    f.write('    pass\n\n\n')

    # Write main routine placeholder
    f.write('# Main routine\n')
    f.write('def main(args):\n')
    f.write('    """ Main docstring """\n')
    f.write('    pass\n\n\n')

    # Write execution section
    f.write('# Make it executable\n')
    f.write("if __name__ == '__main__':\n\n")
    f.write('    # Initialize Parser\n')
    f.write('    parser = ArgumentParser()\n\n')
    f.write('    # Insert arguments here\n\n')
    f.write('    # Link to parser\n')
    f.write('    args = parser.parse_args()\n')
    f.write('    main(args)\n')


# Make it executable
if __name__ == '__main__':

    # Initialize Parser
    parser = ArgumentParser()
    parser.add_argument('name', help = 'Name of function to create')

    # Link to command inputs
    args = parser.parse_args()
    main(args)
