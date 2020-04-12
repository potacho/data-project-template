#!/usr/bin/env python
# coding: utf-8

# In[2]:


import os
import ray
import time
import re
import pandas as pd
import urllib.request
import sys
from itertools import chain
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary
from selenium.common.exceptions import NoSuchElementException


# In[3]:



def scroll_shim(passed_in_driver, object):
    x = object.location['x']
    y = object.location['y']
    scroll_by_coord = 'window.scrollTo(%s,%s);' % ( x, y)
    scroll_nav_out_of_way = 'window.scrollBy(0, -73);'
    passed_in_driver.execute_script(scroll_by_coord)
    passed_in_driver.execute_script(scroll_nav_out_of_way)
    

def asignar_variables_carrefour(features):
    
    title = price = main_image = marca = tipo = dimensiones = float('nan')
        
    i = 0 
    
    for feature in features:
        i = i + 1
        
        
        if feature == 'Características':
            caracteristicas = features[i]
        elif feature == 'Tipo':
            tipo = features[i]
        elif feature == 'Dimensiones del producto (AltoxAnchoXFondo)':
            dimensiones = features[i]
        
    
    return caracteristicas , tipo , dimensiones



def bullet_points(all_bullets): 
    
    bullet1 = bullet2 = bullet3 = bullet4 = bullet5 = bullet6 = bullet7 = bullet8 =  float('nan') 
    
    if len(all_bullets.split("\n")) == 8: 
        bullet1, bullet2, bullet3, bullet4, bullet5, bullet6, bullet7, bullet8= [str(e) for e in all_bullets.split("\n")]
    elif len(all_bullets.split("\n")) == 7: 
        bullet1, bullet2, bullet3, bullet4, bullet5, bullet6, bullet7= [str(e) for e in all_bullets.split("\n")] 
    elif len(all_bullets.split("\n")) == 6: 
        bullet1, bullet2, bullet3, bullet4, bullet5, bullet6 = [str(e) for e in all_bullets.split("\n")] 
    elif len(all_bullets.split("\n")) == 5: 
        bullet1, bullet2, bullet3, bullet4, bullet5 = [str(e) for e in all_bullets.split("\n")] 
    elif len(all_bullets.split("\n")) == 4: 
        bullet1, bullet2, bullet3, bullet4 = [str(e) for e in all_bullets.split("\n")] 
    elif len(all_bullets.split("\n")) == 3: 
        bullet1, bullet2, bullet3, = [str(e) for e in all_bullets.split("\n")]
    elif len(all_bullets.split("\n")) == 2: 
        bullet1, bullet2 = [str(e) for e in all_bullets.split("\n")]
    elif len(all_bullets.split("\n")) == 1: 
        bullet1 = [str(e) for e in all_bullets.split("\n")]
    
    return bullet1, bullet2, bullet3, bullet4, bullet5, bullet6, bullet7, bullet8  


def asignar_variables_amazon(detalles_tecnicos, detalles_usuarios_amazon):
    title = price = bullet1 = bullet2 = bullet3 = bullet4 = bullet5 = bullet6 = bullet7 = bullet8 = main_image = marca = numero_de_modelo = valoracion = clasificacion = producto_desde = float('nan')
        
    for detalle_tecnico in detalles_tecnicos:
        if detalle_tecnico[0] == 'Marca':
            marca = detalle_tecnico[1]
        elif detalle_tecnico[0] == 'Número de modelo':
            numero_de_modelo = detalle_tecnico[1]
        elif detalle_tecnico[0] == 'Valoración media de los clientes':
            valoracion = detalle_tecnico[1]
        elif detalle_tecnico[0] == 'Clasificación en los más vendidos de Amazon':
            clasificacion = detalle_tecnico[1]
        elif detalle_tecnico[0] == 'Producto en Amazon.es desde':
            producto_desde = detalle_tecnico[1]
    
    for detalle_usuarios_amazon in detalles_usuarios_amazon:
        
        if detalle_usuarios_amazon[0] == 'Marca':
            marca = detalle_usuarios_amazon[1]
        elif detalle_usuarios_amazon[0] == 'Número de modelo':
            numero_de_modelo = detalle_usuarios_amazon[1]
        elif detalle_usuarios_amazon[0] == 'Valoración media de los clientes':
            valoracion = detalle_usuarios_amazon[1]
        elif detalle_usuarios_amazon[0] == 'Clasificación en los más vendidos de Amazon':
            clasificacion = detalle_usuarios_amazon[1]
        elif detalle_usuarios_amazon[0] == 'Producto en Amazon.es desde':
            producto_desde = detalle_usuarios_amazon[1]
    
    return marca, numero_de_modelo, valoracion, clasificacion, producto_desde


def asignar_variables_ebay(detalles_tecnicos_1, detalles_tecnicos_2, detalles_tecnicos_3, detalles_tecnicos_4, detalles_tecnicos_5, detalles_tecnicos_6, detalles_tecnicos_7):
    
    title = price = main_image = estado = marca = tipo = caracteristicas = float('nan')
        
    
    for detalle_tecnico in detalles_tecnicos_1:
        if detalle_tecnico[0] == 'Estado:':
            estado = detalle_tecnico[1]
        elif detalle_tecnico[0] == 'Marca:':
            marca = detalle_tecnico[1]
        elif detalle_tecnico[0] == 'Tipo:':
            tipo = detalle_tecnico[1]
        elif detalle_tecnico[0] == 'CaracterÃ\xadsticas:':
            caracteristicas = detalle_tecnico[1]
      
    
    for detalle_tecnico in detalles_tecnicos_2:
        if detalle_tecnico[0] == 'Estado:':
            estado = detalle_tecnico[1]
        elif detalle_tecnico[0] == 'Marca:':
            marca = detalle_tecnico[1]
        elif detalle_tecnico[0] == 'Tipo:':
            tipo = detalle_tecnico[1]
        elif detalle_tecnico[0] == 'CaracterÃ\xadsticas:':
            caracteristicas = detalle_tecnico[1]
      
    for detalle_tecnico in detalles_tecnicos_3:
        if detalle_tecnico[0] == 'Estado:':
            estado = detalle_tecnico[1]
        elif detalle_tecnico[0] == 'Marca:':
            marca = detalle_tecnico[1]
        elif detalle_tecnico[0] == 'Tipo:':
            tipo = detalle_tecnico[1]
        elif detalle_tecnico[0] == 'CaracterÃ\xadsticas:':
            caracteristicas = detalle_tecnico[1]
      
            
    for detalle_tecnico in detalles_tecnicos_4:
        if detalle_tecnico[0] == 'Estado:':
            estado = detalle_tecnico[1]
        elif detalle_tecnico[0] == 'Marca:':
            marca = detalle_tecnico[1]
        elif detalle_tecnico[0] == 'Tipo:':
            tipo = detalle_tecnico[1]
        elif detalle_tecnico[0] == 'CaracterÃ\xadsticas:':
            caracteristicas = detalle_tecnico[1]
      
            
    for detalle_tecnico in detalles_tecnicos_5:
        if detalle_tecnico[0] == 'Estado:':
            marca = detalle_tecnico[1]
        elif detalle_tecnico[0] == 'Marca:':
            numero_de_modelo = detalle_tecnico[1]
        elif detalle_tecnico[0] == 'Tipo:':
            valoracion = detalle_tecnico[1]
        elif detalle_tecnico[0] == 'CaracterÃ\xadsticas:':
            clasificacion = detalle_tecnico[1]
            
    for detalle_tecnico in detalles_tecnicos_6:
        if detalle_tecnico[0] == 'Estado:':
            estado = detalle_tecnico[1]
        elif detalle_tecnico[0] == 'Marca:':
            marca = detalle_tecnico[1]
        elif detalle_tecnico[0] == 'Tipo:':
            tipo = detalle_tecnico[1]
        elif detalle_tecnico[0] == 'CaracterÃ\xadsticas:':
            caracteristicas = detalle_tecnico[1]
      
            
    for detalle_tecnico in detalles_tecnicos_7:
        if detalle_tecnico[0] == 'Estado:':
            estado = detalle_tecnico[1]
        elif detalle_tecnico[0] == 'Marca:':
            marca = detalle_tecnico[1]
        elif detalle_tecnico[0] == 'Tipo:':
            tipo = detalle_tecnico[1]
        elif detalle_tecnico[0] == 'CaracterÃ\xadsticas:':
            caracteristicas = detalle_tecnico[1]
      
    
    return estado, marca, tipo, caracteristicas


def feature_function(features):
    features_list=features.split("\n")
    long=len(features_list)
    count_till= 40  
    while long < count_till:
        features_list.append(float('nan'))
        long+=1
    return features_list


def initialize_eci_info_df():
    
    eci_info = pd.DataFrame(columns = ['item_name.value', 
                                                          'list_price.value_with_tax', 
                                                          'main_image','features','more_features'
                                                         ])
    return eci_info



def initialize_carrefour_info_df():
    
    carrefour_info = pd.DataFrame(columns = ['item_name.value', 
                                                          'list_price.value_with_tax', 
                                                          'main_image', 'caracteristicas',
                                                          'tipo', 'dimensiones'
                                                         ])
    return carrefour_info


def initialize_ebay_info_df():
    
    
    ebay_info = pd.DataFrame(columns = ['item_name.value', 
                                                          'list_price.value_with_tax', 
                                                          'main_image', 'estado', 'marca',
                                                          'tipo','caracteristicas'
                                                         ])
    return ebay_info



def initialize_amazon_info_df():
    
    amazon_info = pd.DataFrame(columns = ['item_name.value', 
                                                          'list_price.value_with_tax' , 'Bullet_point.value',
                                                          'Bullet_point#2.value','Bullet_point#3.value',
                                                          'Bullet_point#4.value', 'Bullet_point#5.value',
                                                          'Bullet_point#6.value','Bullet_point#7.value',
                                                          'main_image','Marca','Número de modelo',
                                                          'Valoración media de los clientes', 
                                                          'Clasificación en los más vendidos de Amazon',
                                                          'Producto en Amazon.es desde'
                                                         ])
    return amazon_info

    
def feature_function(features):
    features_list=features.split("\n")
    long=len(features_list)
    count_till= 40  
    while long < count_till:
        features_list.append(float('nan'))
        long+=1
    return features_list


def initialize_eci_info_df():
    
    eci_info = pd.DataFrame(columns = ['item_name.value', 
                                                          'list_price.value_with_tax', 
                                                          'main_image','features','more_features'
                                                         ])
    return eci_info


# In[4]:


os.environ['PATH'] = f'{os.environ["PATH"]}:{os.getcwd()}/drivers'

ean_list_string= "%s" % (sys.argv[1])
ean_list=ean_list_string.split(", ")

# In[5]:


ray.init()


@ray.remote

def carrefour(ean_list):
    
    
    carrefour_info = initialize_carrefour_info_df()


    for ean in ean_list:
        
        title = price = main_image = caracteristicas = tipo = dimensiones = float('nan')

        
        browser = webdriver.Firefox()
        browser.get('https://www.carrefour.es/')
        
        time.sleep(3)

        action = ActionChains(browser)
        click_browser  = browser.find_element_by_xpath('//input[@id="atg_store_searchInput"]')
        action.move_to_element((click_browser)).click().perform()

        time.sleep(3)

        search = browser.find_element_by_xpath('//input[@class="ebx-search-box__input ebx-search-box__input-query"]')
        search.clear()
        search.send_keys(ean)
        search.send_keys(Keys.ENTER)

        time.sleep(3)
        
        try: 

            action = ActionChains(browser)
            click_image  = browser.find_element_by_xpath("(//img[@class='ebx-result-figure__img'])")
            action.move_to_element((click_image)).click().perform()

        except NoSuchElementException:
            
            print(f"Item {ean} not found")
            
        
        time.sleep(3)
        
        try: 

            title = browser.find_elements_by_xpath('//h1[@class="product-header__name"]')[0].text
        
        except NoSuchElementException:
            
            print(f"title {ean} not found")
            
        except IndexError:
            
            print(f"title {ean} not found")
            
            
        
        try: 
            
            price = browser.find_elements_by_xpath('//span[@class="buybox__price--current"]')[0].text
        
        except NoSuchElementException:
            
            price = browser.find_elements_by_xpath('//span[@class="buybox__price"]')[0].text

        except NoSuchElementException:
            
            print(f"price {ean} not found")
        
        except IndexError:
            
            print(f"price {ean} not found")
            
        
        try: 
            
            main_image = browser.find_element_by_xpath('//img[@class="main-image__image"]').get_attribute('src')

        
        except NoSuchElementException:
            
            print(f"main image {ean} not found")
        
        except IndexError:
            
            print(f"main image {ean} not found")
            
        
        try: 
            
            action = ActionChains(browser)
            click_view_more  = browser.find_element_by_xpath("(//p[@class='product-details__show'])")
            if 'firefox' in browser.capabilities['browserName']:
                scroll_shim(browser, click_view_more)
            action.move_to_element((click_view_more)).click().perform()
            
            time.sleep(1)
            
            features = browser.find_elements_by_xpath('//div[@class="product-details"]')[0].text
            features_list=features.split("\n")

            caracteristicas, tipo, dimensiones = asignar_variables_carrefour(features_list)
            
        except NoSuchElementException:
            
            print(f"features image {ean} not found")
        
        except IndexError:
            
            print(f"features image {ean} not found")
        

        
        carrefour_info.loc[ean] = [title, price, main_image, caracteristicas, tipo , dimensiones]
        
        
        browser.close()
    
    return carrefour_info


@ray.remote



def ebay(ean_list):
    
    ebay_info = initialize_ebay_info_df()
            
    browser = webdriver.Firefox()
    browser.get('https://www.ebay.es/')
    
    time.sleep(3)
   
    for ean in ean_list:
        
        title = price = main_image = estado = marca = tipo = caracteristicas = float('nan')

        search = browser.find_element_by_xpath('//input[@class="gh-tb ui-autocomplete-input"]')
        search.clear()
        search.send_keys(ean)
        search.send_keys(Keys.ENTER)

        time.sleep(3)
        
        try: 

            action = ActionChains(browser)
            click_image  = browser.find_element_by_xpath("(//img[@class='img'])[1]")
            action.move_to_element((click_image)).click().perform()

        
        except NoSuchElementException:
            
            print(f"Item {ean} not found")
        
        
        time.sleep(3)

        
        try:
            
            title = browser.find_elements_by_xpath('//h1[@id="itemTitle"]')[0].text
            
        except NoSuchElementException:
            
            print(f"title {ean} not found")
            
        except IndexError:
            
            print(f"title {ean} not found")
            
        
        try: 
            
            price = browser.find_elements_by_xpath('//span[@id="prcIsum"]')[0].text
            
           
        except NoSuchElementException:
            
            print(f"price {ean} not found")
        
        except IndexError:
            
            print(f"price {ean} not found")
            
        
        try: 
            
            main_image = browser.find_element_by_xpath('//img[@id="icImg"]').get_attribute('src')

        except NoSuchElementException:
            
            print(f"main image {ean} not found")
        
        except IndexError:
            
            print(f"main image {ean} not found")
            
            
        try: 
            
            url = str(browser.current_url)
            time.sleep(3)
            lista = pd.read_html(url, match='.+', flavor = None, header = None, index_col =None, skiprows=None, attrs=None, parse_dates=False, thousands=', ', encoding=None, decimal='.', converters=None, na_values=None, keep_default_na=True, displayed_only=True)
            time.sleep(3)
            
            detalles_tecnicos_1 = lista[10].values.tolist()   
            detalles_tecnicos_2 = lista[11].values.tolist() 
            detalles_tecnicos_3 = lista[12].values.tolist()   
            detalles_tecnicos_4= lista[13].values.tolist()
            detalles_tecnicos_5= lista[14].values.tolist()
            detalles_tecnicos_6= lista[15].values.tolist()
            detalles_tecnicos_7= lista[15].values.tolist()

            estado, marca, tipo, caracteristicas = asignar_variables_ebay(detalles_tecnicos_1, detalles_tecnicos_2, detalles_tecnicos_3, detalles_tecnicos_4, detalles_tecnicos_5, detalles_tecnicos_6, detalles_tecnicos_7)
                                
        
        except urllib.error.HTTPError:
            
            print(f"detalles tecnicos {ean} not found")
        
        except NoSuchElementException:
            
            print(f"detalles tecnicos {ean} not found")


        
        except IndexError:
            
            print(f"detalles tecnicos {ean} not found")
    
    
        ebay_info.loc[ean] = [title, price, main_image, estado, marca, tipo, caracteristicas]

            
    browser.close()
        
            
    return  ebay_info


@ray.remote


def amazon(ean_list):
    
    amazon_info = initialize_amazon_info_df()
            
    browser = webdriver.Firefox()
    browser.get('https://www.amazon.es')
    
    time.sleep(3)
    
    for ean in ean_list:
        
        title = price = bullet1 = bullet2 = bullet3 = bullet4 = bullet5 = bullet6 = bullet7 = bullet8 = main_image = marca = numero_de_modelo = valoracion = clasificacion = producto_desde = float('nan')

        
        search = browser.find_element_by_xpath('//input[@id="twotabsearchtextbox"]')
        search.clear()
        search.send_keys(ean)
        search.send_keys(Keys.ENTER)

        time.sleep(3)
        
        
        try:
    
            action = ActionChains(browser)
            click_image  = browser.find_element_by_xpath("(//div[@class='a-section aok-relative s-image-fixed-height'])")
            action.move_to_element((click_image)).click().perform()
        
        except NoSuchElementException:
            
            print(f"Item {ean} not found")
        
        
        try: 
            
            action = ActionChains(browser)
            click_image  = browser.find_element_by_xpath("(//div[@class='a-section aok-relative s-image-square-aspect'])")
            action.move_to_element((click_image)).click().perform()
            
         
        except NoSuchElementException:
            
            print(f"Item {ean} not found")
        
        
        try: 
            
            action = ActionChains(browser)
            click_image  = browser.find_element_by_xpath("(//div[@class='a-section aok-relative s-image-tall-aspect'])")
            action.move_to_element((click_image)).click().perform()

        except NoSuchElementException:
            
            print(f"Item {ean} not found")
        
        
        time.sleep(3)
        
        
        try: 
            
            title = browser.find_elements_by_xpath('//h1[@id="title"]')[0].text
        
        except NoSuchElementException:
            
            print(f"title {ean} not found")
            
        except IndexError:
            
            print(f"title {ean} not found")
            
            
        try: 
            
            price = browser.find_elements_by_xpath('//span[@id="priceblock_ourprice"]')[0].text
            
        except NoSuchElementException:
            
            price = browser.find_elements_by_xpath('//span[@id="priceblock_dealprice"]')[0].text
            
        except NoSuchElementException:
            
            price = browser.find_elements_by_xpath('//span[@id="priceblock_saleprice"]')[0].text
            
        except NoSuchElementException:
            
            print(f"price {ean} not found")
        
        except IndexError:
            
            print(f"price {ean} not found")
            
            
        
        try:
            
            all_bullets = browser.find_elements_by_xpath('//div[@id="feature-bullets"]')[0].text
            bullet1, bullet2, bullet3, bullet4, bullet5, bullet6, bullet7, bullet8 = bullet_points(all_bullets)
        
        except NoSuchElementException:
            
            print(f"bullets {ean} not found")
        
        except IndexError:
            
            print(f"bullets {ean} not found")
            
        
        try: 
            
            main_image = browser.find_element_by_xpath('//img[@id="landingImage"]').get_attribute('src')
    
        except NoSuchElementException:
            
            print(f"main image {ean} not found")
        
        except IndexError:
            
            print(f"main image {ean} not found")
            
            
        try:
            
            url = str(browser.current_url)
            time.sleep(3)
            lista = pd.read_html(url, match='.+', flavor = None, header = None, index_col =None, skiprows=None, attrs=None, parse_dates=False, thousands=', ', encoding=None, decimal='.', converters=None, na_values=None, keep_default_na=True, displayed_only=True)
            time.sleep(3)

            detalles_tecnicos = lista[1].values.tolist()   
            detalles_usuarios_amazon = lista[2].values.tolist()  

            marca, numero_de_modelo, valoracion, clasificacion, producto_desde = asignar_variables_amazon(detalles_tecnicos, detalles_usuarios_amazon)

                    
            
        except urllib.error.HTTPError:
            print(f"detalles tecnicos {ean} not found")
            
        
        except NoSuchElementException:
            
            print(f"detalles tecnicos {ean} not found")
        
        except IndexError:
            
            print(f"detalles tecnicos {ean} not found")
                
        amazon_info.loc[ean] = [title, price, bullet1, bullet2, bullet3, bullet4, bullet5, bullet6, bullet7, main_image, marca, numero_de_modelo, valoracion, clasificacion, producto_desde]
        
        
    browser.close()

    return amazon_info

'''

@ray.remote


def eci(ean_list):
    
    eci_info = initialize_eci_info_df()
    
    browser = webdriver.Firefox()
    browser.get('https://www.elcorteingles.es/')

    time.sleep(3)

    
    for ean in ean_list:
        
        
        title = price = main_image = features = more_features = float('nan')
        
    
        search = browser.find_element_by_xpath('//input[@id="search-box"]')
        search.clear()
        search.send_keys(ean)
        search.send_keys(Keys.ENTER)

        time.sleep(3)
        
        
        try:

            title = browser.find_elements_by_xpath('//h2[@class="title"]')[0].text
            
            
        except NoSuchElementException:
            
            print(f"title {ean} not found")
            
        except IndexError:
            
            print(f"title {ean} not found")
            
        
        
        try: 
            
            price = browser.find_elements_by_xpath('//div[@class="product-price "]')[0].text
            price_list=price.split("€")
            price = price_list[0]
        
        except NoSuchElementException:
            
            print(f"price {ean} not found")
        
        except IndexError:
            
            print(f"price {ean} not found")
            
        
        try: 
            
             main_image = browser.find_element_by_xpath('//img[@id="product-image-placer"]').get_attribute('src')

        except NoSuchElementException:
            
            print(f"main image {ean} not found")
        
        except IndexError:
            
            print(f"main image {ean} not found")
            
        
        
        try: 
            
            customer_reviews = browser.find_elements_by_xpath('//button[@id="star-button"]')
            for my_aria_label in customer_reviews:
                customer_reviews =my_aria_label.get_attribute("aria-label")
        
        except NoSuchElementException:
            
            print(f" customer reviews {ean} not found")
        
        except IndexError:
            
            print(f" customer reviews  image {ean} not found")
            

        try:

            action = ActionChains(browser)
            click_view_more  = browser.find_element_by_xpath("(//span[@id='text-view-more'])")
            
            if 'firefox' in browser.capabilities['browserName']:
                scroll_shim(browser, click_view_more)
            action.move_to_element((click_view_more)).click().perform()

         
        except NoSuchElementException:
            
            print("IMPOSILE TO SCROLL")
                        
            
        except IndexError:
            
            print("IMPOSILE TO SCROLL")
        
        
        
        try:   
            
            features = browser.find_elements_by_xpath('//div[@id="features"]')[0].text
        
        
        except NoSuchElementException:
            
            print(f" features {ean} not found")
                        
            
        except IndexError:
            
            print(f" features {ean} not found")
            
            
        
        try:
            
            more_features = browser.find_elements_by_xpath('//div[@id="inpage_container"]')[0].text

        
        except NoSuchElementException: 

            print(f" more features {ean} not found")
            
            
        except IndexError:
            
            print(f" more features {ean} not found")
            
            
        
        eci_info.loc[ean] = [title, price, main_image, features, more_features]
    
    
    browser.close()
    
    return eci_info
'''

ret_id1 = carrefour.remote(ean_list)
ret_id2 = ebay.remote(ean_list)
ret_id3 = amazon.remote(ean_list)
#ret_id4 = eci.remote(ean_list)


carrefour_info, ebay_info, amazon_info = ray.get([ret_id1, ret_id2, ret_id3])

print(carrefour_info)
print(ebay_info)
print(amazon_info)