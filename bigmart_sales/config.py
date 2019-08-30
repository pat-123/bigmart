# -*- coding: utf-8 -*-
"""
Created on Tue Aug 13 13:34:22 2019

@author: PAT
"""

from pathlib import Path

data_dir = Path('C:/Users/PAT/Documents/edwisor/projects/bigmart_sales/data/raw')
test_data_path = data_dir  / 'test.csv'
train_data_path = data_dir  / 'train.csv'
submitted_data_path = data_dir / '../submitted/submission.csv'
processed_data_path = data_dir / '../processed/processed.csv'
