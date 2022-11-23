#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on 20201120

@author: dingfengwu

packages:
install.packages('MatchIt') # R package
pip install rpy2==3.2.2
pip install tzlocal

references:
http://www.360doc.com/content/17/1129/16/95144_708343053.shtml
https://zhuanlan.zhihu.com/p/145170602
"""
import warnings
warnings.filterwarnings("ignore")
import os
import sys
import random
import time
import copy
import shutil
import numpy as np
import pandas as pd
from scipy import stats
import statsmodels.stats.multitest as multi
import statsmodels.api as sm
from PIL import Image
import matplotlib.pyplot as plt
import seaborn as sns
from matplotlib import gridspec
import matplotlib.lines as mlines
import configparser
from sklearn.decomposition import PCA
### rpy2
import rpy2.robjects as ro
from rpy2.robjects import r, pandas2ri
from rpy2.robjects.packages import importr
from rpy2.robjects.pandas2ri import py2rpy, rpy2py
pandas2ri.activate()

class micpsm():
    def __init__(self):
        self.base_dir = os.path.dirname(os.path.realpath('__file__'))
        self.config = self.load_config()
        # import packages
        importr('base')
        importr('MatchIt')
        importr('cobalt')
        importr('grDevices')
        
    

def test():
    psm = micrpsm()
    data = psm.create_test_data()
    match_drop_unmatched, match, pairs, sum_matched, balance_stats = psm.propensity_score_match(data, target='Group', features=['F1', 'F2', 'F3'])
    print(psm.diff_by_rank_sum(data, target='Group', features=['F1', 'F2', 'F3']))
    print(psm.diff_by_signed_rank(data, pairs, target='Group', features=['F1', 'F2', 'F3']))
    
if __name__ == '__main__':
    pass
    #test()
