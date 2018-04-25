# -*- coding: utf-8 -*-
"""
Created on 2018.4.10

@author: Wanghui
"""
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

import pylab
import statsmodels.api as sm
import scipy.stats as stats

df = pd.read_csv('NFL Play by Play 2009-2017 (v4).csv', low_memory=False)
label_nominal=['GameID',
               'FieldGoalResult',
               'PlayType']
label_nums = ['PosTeamScore',
              'DefTeamScore','PlayTimeDiff'
              ]
df_nomi = df[label_nominal]#标称属性
df_nums = df[label_nums]#数值属性

#1.标称属性分析

def Nomi(df):
    df_nomi =df
    nominals = df_nomi.value_counts()#频数
    nominals = pd.DataFrame(nominals)
    nominals.to_csv('{}.txt'.format(df.name),sep=':')
    print("EOF")
    return

#------------------------------------------------------------
    #2.1数值属性分析
def num_analysis(df):
    print('------',df.name,'-------')
    nulltotal = df.isnull().sum()
    print('Loss:\n',nulltotal)
    print('Max:\n',df.max())
    print('Min:\n',df.min())
    print('Mean:\n',df.mean())
    print('Median:\n',df.median())
    print('Quantilty:25%\n',df.dropna().quantile(0.25))
    print('Quantilty:50%\n', df.dropna().quantile(0.5))
    print('Quantilty:75%\n', df.dropna().quantile(0.75))
    # q_up = df.quantile(0.25)
    # q_mid = df.quantile(0.5)
    # q_down = df.quantile(0.75)
    # print('Quantilty:25%, 50%, 75%:\n',q_up,q_mid,q_down)
    # num_up = pd.DataFrame(q_up)
    # num_mid = pd.DataFrame(q_mid)
    # num_down = pd.DataFrame(q_down)
    # four_num = pd.merge(num_up,num_mid,left_index=True,right_index=True)
    # four_num = pd.merge(four_num,num_down,left_index=True,right_index=True)
    # print(four_num)

    return

 #2.2数据可视化
#可视化
def visulization(df):
    df=df.dropna()
    def hist(df):
        plt.hist(df,bins=50)
        plt.title('Histgram of {}'.format(df.columns.values))
        plt.show()
    # #print(dfPTScore)
    def drawbox(df):
        plt.boxplot([df])
        plt.title('Boxplot of {}'.format(df.columns.values))
        plt.show()
    df.hist(bins=50)
    sm.qqplot(df, line='45')
    # hist(df)
    pylab.show()
    drawbox(df)
    return

# #2.3缺失值处理
def DataProcess(df_data):
    #原数据
    data=df_data.fillna(0)
    #滤除缺失数据
    df_1 = df_data.dropna()
    Draw(df_data,df_1)

    #用中位数代替缺失值
    df_2 = df_data.fillna(df_data.median())
    Draw(data,df_2)

    #用均值代替缺失值
    df_3 = df_data.fillna(df_data.mean())
    Draw(data,df_3)

    #用众数代替缺失值
    df_3 = df_data.fillna(df_data.mode())
    Draw(data,df_3)

def Draw(df,df1):
    fig=plt.figure()
    ax1=fig.add_subplot(2,2,1)
    ax2 = fig.add_subplot(2, 2, 2)
    #hist
    ax1.boxplot([df],labels=['before'])
    ax2.boxplot([df1],labels=['after'])
    #ax2.title('after')
    # plt.plot(df,'k--',label='before')
    # plt.plot(df1,'k-',label='after')
    plt.show()


if __name__=='__main__':
#标称数据
    # Nomi(df['PlayType'])
    # Nomi(df['GameID'])
    # Nomi(df['FieldGoalResult'])
#数值数据
    # num_analysis(df['PosTeamScore'])
    # num_analysis(df['DefTeamScore'])
    # num_analysis(df['PlayTimeDiff'])
#可视化
    #visulization(df[['PlayTimeDiff']])
#缺省值预处理

    #print(df[['PlayTimeDiff']].dropna().mode())
    DataProcess(df[['PosTeamScore']])
#     DataProcess(dfDTScore,'DefTeamScore')

