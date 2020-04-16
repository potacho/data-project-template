#!/usr/bin/env python
# coding: utf-8

# In[4]:


import pandas as pd 
import sys


ean_list_string= "%s" % (sys.argv[1])
ean_list=ean_list_string.split(", ")


carrefour_info_maxdata=len(ean_list)*6
ebay_info_maxdata=len(ean_list)*7
amazon_info_maxdata=len(ean_list)*15
eci_info_maxdata=len(ean_list)*5


carrefour_info= pd.read_csv('/Users/Abacuc/Project_IH_Abacuc/csv/carrefour_info.csv')
ebay_info= pd.read_csv('/Users/Abacuc/Project_IH_Abacuc/csv/ebay_info.csv')
amazon_info = pd.read_csv('/Users/Abacuc/Project_IH_Abacuc/csv/amazon_info.csv')
eci_info = pd.read_csv('/Users/Abacuc/Project_IH_Abacuc/csv/eci_info.csv')


carrefour_info_nan=carrefour_info.isna().sum().sum()
ebay_info_nan=ebay_info.isna().sum().sum()
amazon_info_nan=amazon_info.isna().sum().sum()
eci_info_nan=eci_info.isna().sum().sum()



carrefour_metric = (carrefour_info_maxdata - carrefour_info_nan) / carrefour_info_maxdata*100
ebay_metric=(ebay_info_maxdata-ebay_info_nan)/ebay_info_maxdata*100
amazon_metric=(amazon_info_maxdata-amazon_info_nan)/amazon_info_maxdata*100
eci_metric=(eci_info_maxdata-eci_info_nan)/eci_info_maxdata*100

data = {
    
    'CARREFOUR': carrefour_metric ,
    'EBAY': ebay_metric,
    'AMAZON': amazon_metric,
    'El CORTE INGLES': eci_metric
}

result= max(data, key=data.get)

output = f"You should star with {result}"

print(output)

