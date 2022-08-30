# -*- coding: utf-8 -*-
"""
    Dfam boilier plate for a module/object

    The Dfam project has settled on using the Black
    styleguide ( https://black.readthedocs.io ).

    NOTE: This is more of a placeholder as we don't currently need
          to standardize a module/class object at this time.  Please
          refer to the dfam_python_script.py boilerplate for current
          Dfam-specific boilerplate.

SEE ALSO: related_module.py
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

# Code comments

class TestClass:

    def __init__(self):
        """TestClass() - basic constructor"""
        self.data = []

    i = 12345

    def f(self):
        """
        f() - perform perfunctory hello world services

        Non PEP 484 function with types documented in
        the docstring.

        Args:
            arg1 (int): Does something cool

        Returns:
            int  : foobar...
        """
        return 'hello world'


    def g(param1: int, param2: str) -> bool:
        """
        g() - perform perfunctory hello world services

        PEP 484 function with types documented in the
        definition -- no need to include in docstring.

        Args:
            param1: Does something cool
            param2: Another cool parameter

        Returns:
            Boolean value indicating success.
        """
        return True


