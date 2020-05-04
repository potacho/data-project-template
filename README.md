# Show me My DATA! 

**Abacuc Mendez**

**Ironhack Madrid Octubre 2019 Part-time**


## Overview :eyes:

The formal title of this project would be: Development of a complete web product, to help SMEs launch their products to the online market

* The objective of this project is to make a complete product, based on a web application, the purpose of which is to help Spanish manufacturing SMEs to launch their products online, through the different e-commerce stores we have in the Spanish marketplace.

* This web application will help the user to extract the characteristics of their products that are present in some e-commerce (Title, description, dimensions, images, etc. ...), currently being sold by one of their distributors. 

* In addition, once the information on the products has been extracted, and based on a previous study of the most important e-commerce, the user will be recommended the e-commerce that they should use to launch their products on the Spanish market.

* To make this recommendation, a python-based model will be used, which will have been prpeared to select the most appropriate option, based on the different characteristics of its products. 

* This will facilitate the direct entry of manufacturing companies to online sales, without the need for intermediaries and to regenerate these existing data. The entry into the ecommerce market will help these companies to increase their income, both nationally and internationally.


![Resultado de imagen de recommendation Systems](https://miro.medium.com/max/2000/1*f2-zeAOSNB4RGlqH9emTlQ.jpeg)

* The project can be use from 2 different displays:
  - Terminal
  - Django based web


## Django web:


* The basic web based in Django Will have the following URLs: 

  -	path(r''): The inital path, in which you need to introduce the bar codes of the Vendor Items. 
    
  -	path(r'data/'): The intermediate path, In which you will see the Data Scraped from the different Ecommerce analyzed. The web display the data using Pandas Dataframe with the corresponding Ecommerce LOGO. 
  
  -	path(r'results/'): After analyzing the Data, and considering the and considering the characteristics of the manufacturer's typical client, the system will show the result of which would be the recommended Ecommerce to start


## Data Scraping :gear:


* The scraping will obtain 4 dataframes, one for each marketplace analyze 

* The 4 dataframes will have the following characteristics:

  1. Amazon dataframe contains information about: 'item_name.value','list_price.value_with_tax' , 'Bullet_point.value','Bullet_point#2.value','Bullet_point#3.value','Bullet_point#4.value', 'Bullet_point#5.value', 'Bullet_point#6.value','Bullet_point#7.value','main_image','Marca','Número de modelo','Valoración media de los clientes','Clasificación en los más vendidos de Amazon', 'Producto en Amazon.es desde'
  
  2. ECI dataframe contains information about:'item_name.value','list_price.value_with_tax', 'main_image','features','more_features'
  
  3. Ebay dataframe contains information about: 'item_name.value','list_price.value_with_tax', 'main_image', 'estado', 'marca', 'tipo','caracteristicas'
  
  4. Carrefour dataframe contains information about: 'item_name.value', 'list_price.value_with_tax', 'main_image', 'caracteristicas','tipo','dimensiones'
  

## Marketplace recomendation

In order to do the recommendation we will use to kind of inputs: 

* Vendor Inputs: We ask the Vendor few inputs in order to know their typical client in order to do an Accurate recommendation 

* Main Ecommerce Inputs :We have previously analyzed the main clients of the most important Ecommerce in order to match the results with the Vendor inputs, the characteristics that have been studied are: 

   1.  % Main categories sold
   
   2.  % Age    
   
   3.  % Men Vs. Women
   
   4.  % community type


### :computer: **Technology stack**

Python, Pandas, Selenium, Ray, Selenium, Django.


### :baby: **Status**


Alpha Version: Ironhack Data Analytics Final Project. 


## :file_folder: **Folder structure**
```
└── Project_IH_Abacuc
    ├── __trash__
    ├── requeriments.txt
    ├── README.md
    ├── notebooks
    │   ├── web_scraping_mm.ipynb
    │	├── web_scraping_eci.ipynb
    │	├── web_scraping_carrefour.ipynb
    │	├── web_scraping_amazon.ipynb
    │   └── web_scraping_ebay.ipynb
    ├── django_app
    │   ├── my_vendors
    │   └── polls 
    └── csv
        ├── mm_info.csv
        ├── eci_info.csv
        ├── carrefour_info.csv
        ├── amazon_info.csv
        └── ebay_info.csv
        
```


## :love_letter: **Contact info**

https://www.linkedin.com/in/abacucmendezsala/

