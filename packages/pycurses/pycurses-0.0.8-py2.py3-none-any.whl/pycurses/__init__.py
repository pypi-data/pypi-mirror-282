""" Python package for making terminal UIs """

import sys
import os
sys.path.append(os.path.join(os.path.dirname(os.path.abspath(__file__)),os.pardir))


from colors import CursesColors
from list_view import ListView
import window
import layout
import mainwindow
import popup


__version__ = "0.0.8"




