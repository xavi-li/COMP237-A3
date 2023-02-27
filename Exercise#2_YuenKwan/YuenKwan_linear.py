# -*- coding: utf-8 -*-
"""
Created on Sun Feb 26 14:08:42 2023

@author: YuenKwan LI (301228849)
"""

import pandas as pd
import os
import matplotlib.pyplot as plt

# Req.c5: Accept a dataframe as an argument and normalizes all the datapoint.
def normalize(dataframe):
    return (dataframe - dataframe.min()) / (dataframe.max() - dataframe.min())


# Req.a: Load data
path = 'C:/workspace/IntroAI/Assignment 3/Exercise#2_YuenKwan'
filename = 'Ecom Expense.csv'
fullpath = os.path.join(path, filename)
ecom_exp_YuenKwan = pd.read_csv(fullpath)


# Req.b: Initial exploration
print('----------- b1) Print first 3 records -------------')
print(ecom_exp_YuenKwan.head(3))
print('----------- b2) Shape of data frame -------------')
print(ecom_exp_YuenKwan.shape)
print('----------- b3) Names, Types, & Counts -------------')
ecom_exp_YuenKwan.info()
print('----------- b4) Refer to Written Response -------------')
'''
 "PassengerId", "Name", "Ticket" columns contain unique values.
 "Cabin" column contains a lot of missing values. 
 These 4 columns are not useful for the model.
'''
print('----------- b5) Unique Values of Sex, Pclass -------------')
print('Sex: ', ecom_exp_YuenKwan['Sex'].unique())
print('Pclass: ', ecom_exp_YuenKwan['Pclass'].unique())
print('----------- End of b) Initial Exploration -------------')

'''
print(ecom_exp_YuenKwan.describe())
'''





