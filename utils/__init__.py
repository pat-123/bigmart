# -*- coding: utf-8 -*-
"""
Created on Tue Sep 4

@author: PAT
"""

import numpy as np
import pandas as pd
import re

from scipy.stats import kurtosis,skew

import seaborn  as sb
import matplotlib.pyplot as plt

from sklearn.model_selection import train_test_split
from sklearn.feature_selection import chi2
from scipy.stats import chi2_contingency
import geopy
from geopy.distance import geodesic

from sklearn.model_selection import KFold
from sklearn.metrics import auc
from sklearn.ensemble import RandomForestRegressor
from sklearn.neighbors import KNeighborsRegressor

from sklearn.metrics import mean_squared_error, r2_score
import statsmodels.api as sm
#from statsmodels.regression.linear_model import OLS
from statsmodels.stats.outliers_influence import variance_inflation_factor
from sklearn.linear_model import LinearRegression
from scipy import stats


