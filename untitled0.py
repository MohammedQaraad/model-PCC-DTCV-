# -*- coding: utf-8 -*-
"""
Created on Sun Apr 18 23:42:05 2021

@author: Mohanmmed
"""


import tarfile
import openpyxl
import pandas as pd
import numpy as np
from scipy.stats import ranksums
from scipy.stats import friedmanchisquare
file='DTACC.xlsx'
df = pd.read_excel(file,header=None)



# !GWO 
auc4 = df[0]
auc5 = df[1]
auc6 = df[2]




print("---------------------------------------Friedman Test")
spRes = friedmanchisquare(auc4,auc5,auc6)
print(spRes)
print(ranksums(auc4, auc5))
# print(ranksums(ssf2, pf2))
# print(ranksums(ssf3, pf3))
# print(ranksums(ssf4, pf4))
# print(ranksums(ssf5, pf5))
# print(ranksums(ssf6, pf6))

# print(scf1 , scf2)
# # print(co.shape)