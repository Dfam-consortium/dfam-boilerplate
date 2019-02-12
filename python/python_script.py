#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
    Usage: ./python-script.py [--help] -myarg1=foo 
                              -myarg2=bar

    Blah...this is a very detailed explanation of the
    this script.

    Args:
        --help, -h  : show this help message and exit
        --myarg1    : this is the first param
        --myarg2    : this is the second param

SEE ALSO: related_script.py
          Dfam: http://www.dfam.org

AUTHOR(S):
    Firstname Lastname <email@domain>

LICENSE:
    This code may be used in accordance with the Creative Commons
    Zero ("CC0") public domain dedication:
    https://creativecommons.org/publicdomain/zero/1.0/

DISCLAIMER:
  This software is provided ``AS IS'' and any express or implied
  warranties, including, but not limited to, the implied warranties of
  merchantability and fitness for a particular purpose, are disclaimed.
  In no event shall the authors or the Dfam consortium members be
  liable for any direct, indirect, incidental, special, exemplary, or
  consequential damages (including, but not limited to, procurement of
  substitute goods or services; loss of use, data, or profits; or
  business interruption) however caused and on any theory of liability,
  whether in contract, strict liability, or tort (including negligence
  or otherwise) arising in any way out of the use of this software, even
  if advised of the possibility of such damage.

"""
# TODO: 
#    * Something...
#
# Style Guide: See Google Python Style Guide
#     http://google.github.io/styleguide/pyguide.html
#

#
# Module imports
# e.g 'from python_module import TestClass'
import sys
import os
import argparse


def _usage():
    """
    _usage() - Print out docstring for this file

    Args:
        None

    Returns:
        Calls help/pydoc with screen pager on this script file
        and exits normally afterwards.
    """
    # Call to help/pydoc with scriptname ( sans path and file extension )
    help(os.path.splitext(os.path.basename(__file__))[0])
    sys.exit(0)

#
# Other subroutines here
#

#
# main subroutine ( protected from import execution )
#
def main(*args):
    #
    # Options processing
    #
    #   There are two ways to document usage/command line 
    #   arguments using this boilerplate.  The intended way
    #   is to document using docstrings at the top of the 
    #   script.  This way the pydoc docs match the output
    #   produced by '-h' or '--help' using the argparse
    #   custom action class ( _CustomUsageAction ) defined
    #   below.  If you want the paired-down argparse default
    #   instead, simply remove the "add_help=False" argument
    #   to the argparse constructor below and comment out
    #   the add_argment('-h', ...) line.
    #
    class _CustomUsageAction(argparse.Action):
        """
        _CustomUsageAction() - Class to call our _usage function
        """
        def __init__(self, option_strings, dest, default=False, required=False, help=None):
            super(_CustomUsageAction, self).__init__( 
                      option_strings=option_strings, dest=dest,
                      nargs=0, const=True, default=default,
                      required=required, help=help) 
        def __call__(self, parser, args, values, option_string=None):
            _usage()

    parser = argparse.ArgumentParser(add_help=False )
    parser.add_argument('-h', '--help', action=_CustomUsageAction )
    #
    # Examples:
    #   e.g. -f 3
    #     parser.add_argument('-f','--foo', type=int, default=42, help='FOO!')
    #   e.g. -f   : If set store True in args.foo
    #     parser.add_argument('-f','--foo', action='store_true')
    #   e.g. Set the -foo parameter as required
    #     parser.add_argument('-f','--foo', type=int, required=True )
    #   e.g. Set the args.foobar using the parameter passed with -foo
    #     parser.add_argument('-f','--foo', dest='foobar', type=int )
    #   e.g. Mutual exclusivity
    #     action = parser.add_mutually_exclusive_group(required=True)
    #     action.add_argument(...)
    #
    args = parser.parse_args()

    #
    # Remaining main() code
    #



#
# Wrap script functionality in main() to avoid automatic execution
# when imported ( e.g. when help is called on file )
#
if __name__ == '__main__':
    main(*sys.argv)
