# import packages  (not every package is used in each notebook template)

# numerical computing
import numpy as np                    # Fundamental package for numerical computing in Python

# uncertainty calculations
from uncertainties import ufloat      # For handling numbers with uncertainties
from uncertainties.umath import *     # For applying mathematical functions with uncertainties
from uncertainties import unumpy      # For handling uncertainties in arrays

# data manipulation and analysis
import pandas as pd                   # Powerful data manipulation and analysis library

# data visualization in tables
from tabulate import tabulate

# data visualization in plots
import matplotlib.pyplot as plt       # Library for creating static, interactive, and animated visualizations

# scientific computing
import scipy as sc                    # Open-source scientific computing library
from scipy.stats import linregress    # For performing linear regression analysis
from scipy.constants import R         # Physical and mathematical constants

# interactive display in Jupyter Notebook
from IPython.display import display, Markdown   # For displaying rich content (e.g., Markdown) in Jupyter Notebook

# standard mathematical functions
import math                          # Python's built-in math functions

# widgets (to create elements such as dynamic input/output boxes)
import ipywidgets as widgets