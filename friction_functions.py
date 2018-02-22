import numpy as np
import scipy.special

import matplotlib
matplotlib.use
import matplotlib.pyplot as plt
plt.style.use('seaborn-talk')

import pandas as pd

def friction_data(file_name, load_gram):
    excel_file = pd.ExcelFile(file_name)
    df = excel_file.parse('Sheet2')
    df.columns = ['reading', 'load', 'travel', 'time']
    df.loc[:, 'load'] *= -1
    df_time_less0 = df[df['load'] <= 0]
    length = len(df_time_less0.index)
    df_time0 = df.iloc[length - 1 :]
    travel0 = df_time0.loc[length-1, 'travel']
    df_time0.loc[:, 'travel'] += -travel0
    df_time0 = df_time0.dropna()
    df_plot = df_time0

    return df_plot

def friction_coefficient(file_name, load_gram):

    df = friction_data(file_name, load_gram)
    length = df['reading'].iloc[0]

    df['dload'] = df['load'] - df['load'].shift(-1)
    length1 = df[df['dload'].gt(0.0)].index[0]
    df_friction = df.iloc[length1-length :]

    #only choose the data 1 cm after the static friction and calculate for 5 cm
    x_s = df_friction['travel'].iloc[0]
    # x_d_1 = x_s + 10
    # x_d_2 = x_d_1 + 50
    # for soda lime wafer
    x_d_1 = x_s + 5
    x_d_2 = x_d_1 + 18
    d_1 = df_friction[df_friction['travel'].gt(x_d_1)].index[0]
    d_2 = df_friction[df_friction['travel'].gt(x_d_2)].index[0]

    mean = df_friction['load'].iloc[d_1-length1:d_2-length1].mean()
    load = load_gram * 9.8 / 1000
    friction_d = mean/load
    friction_s = df_friction.loc[length1-1, 'load']/load

    return friction_d, friction_s
