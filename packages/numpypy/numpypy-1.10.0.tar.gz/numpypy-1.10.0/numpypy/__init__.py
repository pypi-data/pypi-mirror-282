r"""
 ________    ___  ___   _____ ______    ________   ___    ___  ________   ___    ___
|\   ___  \ |\  \|\  \ |\   _ \  _   \ |\   __  \ |\  \  /  /||\   __  \ |\  \  /  /|
\ \  \\ \  \\ \  \\\  \\ \  \\\__\ \  \\ \  \|\  \\ \  \/  / /\ \  \|\  \\ \  \/  / /
 \ \  \\ \  \\ \  \\\  \\ \  \\|__| \  \\ \   ____\\ \    / /  \ \   ____\\ \    / /
  \ \  \\ \  \\ \  \\\  \\ \  \    \ \  \\ \  \___| \/  /  /    \ \  \___| \/  /  /
   \ \__\\ \__\\ \_______\\ \__\    \ \__\\ \__\  __/  / /       \ \__\  __/  / /
    \|__| \|__| \|_______| \|__|     \|__| \|__| |\___/ /         \|__| |\___/ /
                                                 \|___|/                \|___|/

NumPyPy
==========

NumPyPy is a Python library that offers a comprehensive set of mathematical tools for numerical computation,
scientific research, and data analysis.

Copyright
==========

- Author: Shen Jiayi
- Email: 2261748025@qq.com
- Copyright: 2023 to perpetuity. All rights reserved.
"""

__author__ = "Shen Jiayi"
__email__ = "2261748025@qq.com"
__copyright__ = "2023 to perpetuity. All rights reserved."

import sys

stdout = sys.stdout
sys.stdout = None

from pypynum import *
from pypynum import __version__ as version

sys.stdout = stdout
__version__ = "1.10.0"
if version != __version__:
    raise RuntimeError("The version {} of PyPyNum does not match the version {} of NumPyPy. "
                       "Please update both packages to the latest version.".format(version, __version__))
print("NumPyPy", "Version -> " + __version__, "It is an alias for PyPyNum",
      "See also PyPI link for PyPyNum -> https://pypi.org/project/PyPyNum/", sep=" | ")


def test():
    from pypynum import test


def this():
    from pypynum import this
