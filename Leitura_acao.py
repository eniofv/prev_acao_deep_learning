# -*- coding: utf-8 -*-
"""
Created on Thu Jul 16 23:23:18 2020

@author: eniov
"""

import pandas as pd
from pandas_datareader import data as web
portifolio = ['VALE3','ITUB4','BBDC4','PETR4']
diretorio = 'C:/EAD/13. TCC/Python/'
extensao = '.txt'
serie = pd.DataFrame()
for acao in portifolio :
  serie = web.DataReader(acao+'.SA', data_source='yahoo', start='2010-1-1' , end='2020-7-16')
  print(serie)
  serie.to_csv(diretorio+acao+extensao)