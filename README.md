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


![Resultado de imagen de recommendation systems](https://miro.medium.com/max/2000/1*f2-zeAOSNB4RGlqH9emTlQ.jpeg)

* The project can be use from 2 different displays:
  - Terminal
  - Django based web


## Django web: 


### Overview



## Data Scraping :gear:


### Overview:

* The scraping will obtain 4 dataframes, one for each marketplace analyze 

* The 4 dataframes will have the following characteristics:

  1. Amazon dataframe contains information about: 'item_name.value','list_price.value_with_tax' , 'Bullet_point.value','Bullet_point#2.value','Bullet_point#3.value','Bullet_point#4.value', 'Bullet_point#5.value', 'Bullet_point#6.value','Bullet_point#7.value','main_image','Marca','Número de modelo','Valoración media de los clientes','Clasificación en los más vendidos de Amazon', 'Producto en Amazon.es desde'
  
  2. ECI dataframe contains information about:'item_name.value','list_price.value_with_tax', 'main_image','features','more_features'
  
  3. Ebay dataframe contains information about: 'item_name.value','list_price.value_with_tax', 'main_image', 'estado', 'marca', 'tipo','caracteristicas'
  
  4. Carrefour dataframe contains information about: 'item_name.value', 'list_price.value_with_tax', 'main_image', 'caracteristicas','tipo','dimensiones'
  


## Data Analysis : Tableau



### Overview


### Marketplace recomendation




## Conclusion



### :file_folder: **Folder structure**
```
└── project
    ├── __trash__
    ├── .gitignore
    ├── .env
    ├── requeriments.txt
    ├── README.md
    ├── main_script.py
    ├── notebooks
    │   ├── notebook1.ipynb
    │   └── notebook2.ipynb
    ├── package1
    │   ├── module1.py
    │   └── module2.py
    └── data
        ├── raw
        ├── processed
        └── results
```


### :love_letter: **Contact info**

https://www.linkedin.com/in/abacucmendezsala/

