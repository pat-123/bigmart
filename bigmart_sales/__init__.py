# -*- coding: utf-8 -*-
"""
Created on Tue Aug 13 13:38:47 2019

@author: PAT
"""


import os
import sys
from sklearn.datasets import load_iris

import pandas as pd
import seaborn  as sb
import matplotlib.pyplot as plt

from pylab import rcParams
rcParams['figure.figsize']=(5,6)
plt.style.use('seaborn-whitegrid')

import numpy as np
from sklearn.preprocessing import LabelEncoder
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeRegressor
from scipy.stats import chi2_contingency
from sklearn.metrics import mean_squared_error, r2_score
from sklearn.feature_selection import SelectKBest
from sklearn.feature_selection import chi2
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import KFold
import sklearn

# add to sys paths
#sys.path.append('C:\\Users\\PAT\\Documents\\edwisor\\projects\\bigmart_sales')
def rt_parent():
    parent_dir = 'TBD---------'
    return parent_dir