#!/usr/bin/env python
# coding: utf-8

# In[4]:


import pandas as pd 
import sys




ean_list_string= "%s" % (sys.argv[1])
ean_list=ean_list_string.split(", ")


#Parameters 

'''
categoria de productos = ('Electrónica y Media', 'Hobby y Juguetes', 'Muebles y Hogar', 'Comida y Cuidado personal', 'Moda')

Edad Media cliente  = ('18-24', '25-34', '35-44', '45-54', '55-64')

Tamaño Familia = ("1","2","3","4","5 o mas")

Tipo de comunidad = ('Comunidades Rurales', 'Pequeños Pueblos', 'Ciudades Medianas', 'Grandes Ciudades', 'Ciudades con mas de 1 millón de habitantes')

'''
#Obtener datos

categoria = sys.argv[2]
edad_media = sys.argv[3]
Tamaño_familia = sys.argv[4]
tipo_comunidad = sys.argv[5]


#Amazon 

Ventas_categoria_amazon={'Electrónica y Media': 0.55, 'Hobby y Juguetes': 0.22, 'Muebles y Hogar': 0.14, 'Comida y Cuidado personal': 0.05, 'Moda': 0.04}
edad_media_cliente_amazon={'18-24': 0.13, '25-34': 0.21, '35-44': 0.25, '45-54': 0.23, '55-64': 0.17}
tamaño_familia_amazon={'1': 0.08,  '2': 0.26, '3': 0.23, '4': 0.32, '5 o mas': 0.11}
tipo_comunidad_amazon={'Comunidades Rurales': 0.06, 'Pequeños Pueblos': 0.18, 'Ciudades Medianas': 0.21, 'Grandes Ciudades': 0.35, 'Ciudades con mas de 1 millón de habitantes': 0.2}

amazon_value=Ventas_categoria_amazon[categoria]*2+edad_media_cliente_amazon[edad_media]+tamaño_familia_amazon[Tamaño_familia]+tipo_comunidad_amazon[tipo_comunidad]


#Carrefour 

Ventas_categoria_Carrefour ={'Electrónica y Media': 0.12, 'Hobby y Juguetes': 0.17, 'Muebles y Hogar': 0.1, 'Comida y Cuidado personal': 0.52, 'Moda': 0.09}
edad_media_cliente_Carrefour ={'18-24': 0.12, '25-34': 0.21, '35-44': 0.29, '45-54': 0.21, '55-64': 0.17}
tamaño_familia_Carrefour ={'1': 0.06, '2': 0.18, '3': 0.3, '4': 0.33, '5 o mas': 0.13}
tipo_comunidad_Carrefour ={'Comunidades Rurales': 0.05, 'Pequeños Pueblos': 0.14, 'Ciudades Medianas': 0.26, 'Grandes Ciudades': 0.37, 'Ciudades con mas de 1 millón de habitantes': 0.19}

carefour_value=Ventas_categoria_Carrefour[categoria]*2+edad_media_cliente_Carrefour[edad_media]+tamaño_familia_Carrefour[Tamaño_familia]+tipo_comunidad_Carrefour[tipo_comunidad]

#eci
Ventas_categoria_eci ={'Electrónica y Media': 0.23, 'Hobby y Juguetes': 0.13, 'Muebles y Hogar': 0.23, 'Comida y Cuidado personal': 0.13, 'Moda': 0.28}
edad_media_cliente_eci ={'18-24': 0.11, '25-34': 0.19, '35-44': 0.3, '45-54': 0.23, '55-64': 0.17}
tamaño_familia_eci ={'1': 0.06, '2': 0.21, '3': 0.29, '4': 0.34, '5 o mas': 0.1}
tipo_comunidad_eci ={'Comunidades Rurales': 0.05, 'Pequeños Pueblos': 0.14, 'Ciudades Medianas': 0.21, 'Grandes Ciudades': 0.42, 'Ciudades con mas de 1 millón de habitantes': 0.19}

eci_value=Ventas_categoria_eci[categoria]*2+edad_media_cliente_eci[edad_media]+tamaño_familia_eci[Tamaño_familia]+tipo_comunidad_eci[tipo_comunidad]


#MediaMarkt

Ventas_categoria_mm  ={'Electrónica y Media': 0.7, 'Hobby y Juguetes': 0.075, 'Muebles y Hogar': 0.22, 'Comida y Cuidado personal': 0.05, 'Moda': 0}
edad_media_cliente_mm  ={'18-24': 0.14, '25-34': 0.24, '35-44': 0.26, '45-54': 0.22, '55-64': 0.13}
tamaño_familia_mm ={'1': 0.06, '2': 0.2, '3': 0.31, '4': 0.34, '5 o mas': 0.1}
tipo_comunidad_mm ={'Comunidades Rurales': 0.04, 'Pequeños Pueblos': 0.14, 'Ciudades Medianas': 0.2, 'Grandes Ciudades': 0.4, 'Ciudades con mas de 1 millón de habitantes': 0.21}

mm_value=Ventas_categoria_mm[categoria]*2+edad_media_cliente_mm[edad_media]+tamaño_familia_mm[Tamaño_familia]+tipo_comunidad_mm[tipo_comunidad]


#ebay 

Ventas_categoria_ebay  ={'Electrónica y Media': 0.2, 'Hobby y Juguetes': 0.2, 'Muebles y Hogar': 0.2, 'Comida y Cuidado personal': 0.2, 'Moda': 0.2}
edad_media_cliente_ebay  ={'18-24': 0.2, '25-34': 0.2, '35-44': 0.2, '45-54': 0.2, '55-64': 0.2}
tamaño_familia_ebay ={'1': 0.2, '2': 0.2, '3': 0.2, '4': 0.2, '5 o mas': 0.2}
tipo_comunidad_ebay ={'Comunidades Rurales': 0.2, 'Pequeños Pueblos': 0.2, 'Ciudades Medianas': 0.2, 'Grandes Ciudades': 0.2, 'Ciudades con mas de 1 millón de habitantes': 0.2}

ebay_value=Ventas_categoria_ebay[categoria]*2+edad_media_cliente_ebay[edad_media]+tamaño_familia_ebay[Tamaño_familia]+tipo_comunidad_ebay[tipo_comunidad]

carrefour_info_maxdata=len(ean_list)*6
ebay_info_maxdata=len(ean_list)*7
amazon_info_maxdata=len(ean_list)*15
eci_info_maxdata=len(ean_list)*5
mm_info_maxdata=len(ean_list)*5


carrefour_info= pd.read_csv('/Users/Abacuc/Project_IH_Abacuc/csv/carrefour_info.csv')
ebay_info= pd.read_csv('/Users/Abacuc/Project_IH_Abacuc/csv/ebay_info.csv')
amazon_info = pd.read_csv('/Users/Abacuc/Project_IH_Abacuc/csv/amazon_info.csv')
eci_info = pd.read_csv('/Users/Abacuc/Project_IH_Abacuc/csv/eci_info.csv')
mm_info = pd.read_csv('/Users/Abacuc/Project_IH_Abacuc/csv/mm_info.csv')


carrefour_info_nan=carrefour_info.isna().sum().sum()
ebay_info_nan=ebay_info.isna().sum().sum()
amazon_info_nan=amazon_info.isna().sum().sum()
eci_info_nan=eci_info.isna().sum().sum()
mm_info_nan=eci_info.isna().sum().sum()


carrefour_metric = (((carrefour_info_maxdata - carrefour_info_nan) / carrefour_info_maxdata)+carefour_value)*100
ebay_metric=(((ebay_info_maxdata-ebay_info_nan)/ebay_info_maxdata)+ebay_value)*100
amazon_metric=(((amazon_info_maxdata-amazon_info_nan)/amazon_info_maxdata)+amazon_value)*100
eci_metric=(((eci_info_maxdata-eci_info_nan)/eci_info_maxdata)+eci_value)*100
mm_metric=(((mm_info_maxdata-eci_info_nan)/mm_info_maxdata)+mm_value)*100

data = {
    
    'CARREFOUR': carrefour_metric ,
    'EBAY': ebay_metric,
    'AMAZON': amazon_metric,
    'El CORTE INGLES': eci_metric,
    'MediaMarkt': mm_metric
}

result= max(data, key=data.get)

output = f"You should star with {result}"

print(output)

