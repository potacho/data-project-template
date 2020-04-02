# Show me My DATA! 

**Abacuc Mendez**

**Ironhack Madrid Octubre 2019 Part-time**


## Overview :eyes:

The formal title of this project would be: Development of a complete web product, to help SMEs launch their products to the online market

* The objective of this project is to make a complete product, based on a web application, the purpose of which is to help Spanish manufacturing SMEs to launch their products online, through the different e-commerce stores we have in the Spanish marketplace.

![Resultado de imagen de recommendation systems](https://miro.medium.com/max/2000/1*f2-zeAOSNB4RGlqH9emTlQ.jpeg)

* The project can be use from 2 different displays:
  - Terminal
  - Django based web

## Data Scraping :gear:

### Overview:

This web application will help the user to extract the characteristics of their products that are present in some e-commerce (Title, description, dimensions, images, etc. ...), currently being sold by one of their distributors. In addition, once the information on the products has been extracted, and based on a previous study of the most important e-commerce, the user will be recommended the e-commerce that they should use to launch their products on the Spanish market. To make this recommendation, a python-based “Machine Learning” model will be used, which will have been trained to select the most appropriate option, based on the different characteristics of its products. This will facilitate the direct entry of manufacturing companies to online sales, without the need for intermediaries and to regenerate these existing data. The entry into the ecommerce market will help these companies to increase their income, both nationally and internationally.

### Overview:

* The dataset is a list of around 45.000 movies, 26 million ratings from over 270.000 users on IMDb.
* We have take or dataset from [Kaggle](https://www.kaggle.com/rounakbanik/the-movies-dataset).
* We have use 2 datasets for this proyect for the moment:
  1. **movies_metadata.csv:** The main Movies Metadata file. Contains information on 45,000 movies featured in the Full MovieLens dataset. Features include posters, backdrops, budget, revenue, release dates, languages, production countries and companies.
  2. **links_small.csv:** Contains the TMDB and IMDB IDs of a small subset of 9,000 movies of the Full Dataset.

### Data Ingestion

* I donwload the data set into my src :file_folder: and call it from the Jupyter Notebook or .py file:

  `md = pd.read_csv('../src/movies_metadata.csv')
  md.head()`

* There are IMDb API availables for python:

  - [IMDbPY](https://pypi.org/project/IMDbPY/)
  - [OMDb](http://www.omdbapi.com/)

### Data Wrangling and Cleaning

* The Data was pretty clean and useful but we need it to make some changes to better suite the propose of the exercise:
  - Use lambda to take the names betweens the [lists brackets] they were on the datasets.
  - Drop the nulls from the vote_count columns.
  -  Split the release dates to only takes the years.
  - Change the vote_count and vote_average and transformed in to int.

## Data Analysis :chart_with_downwards_trend: :mag:

### Overview

To be able to make a Resommendation System you need to feed the system with as much numeric data as possible to be able to calculate de distances between movies, this way the query will be as accurate as possible.

### Simple Recommender

The Simple Recommender offers generalized recommnendations to every user based on movie popularity and (sometimes) genre. The basic idea behind this recommender is that movies that are more popular and more critically acclaimed will have a higher probability of being liked by the average audience. This model does not give personalized recommendations based on the user.

The implementation of this model is extremely trivial. All we have to do is sort our movies based on ratings and popularity and display the top movies of our list. As an added step, we can pass in a genre argument to get the top movies of a particular genre.

I use the TMDB Ratings to come up with our Top Movies Chart. I will use IMDB's weighted rating formula to construct my chart. Mathematically, it is represented as follows:

Weighted Rating (WR) = (vv+m.R)+(mv+m*C) where,

v is the number of votes for the movie m is the minimum votes required to be listed in the chart R is the average rating of the movie C is the mean vote across the whole report.

```python
def weighted_rating(x):    
   v = x['vote_count']    
   R = x['vote_average']    
   return (v/(v+m) * R) + (m/(m+v) * C)
 
qualified['wr'] = qualified.apply(weighted_rating, axis=1)
qualified = qualified.sort_values('wr',ascending=False).head(250)
```

### Content Based Recommende

The recommender we built in the previous section suffers some severe limitations. For one, it gives the same recommendation to everyone, regardless of the user's personal taste. If a person who loves romantic movies (and hates action) were to look at our Top 15 Chart, s/he wouldn't probably like most of the movies. If s/he were to go one step further and look at our charts by genre, s/he wouldn't still be getting the best recommendations.

To personalise our recommendations more, I am going to build an engine that computes similarity between movies based on certain metrics and suggests movies that are most similar to a particular movie that a user liked. Since we will be using movie metadata (or content) to build this engine, this also known as Content Based Filtering.

I will build two Content Based Recommenders based on:

- Movie Overviews and Taglines
- Movie Cast, Crew, Keywords and Genre

Also, as mentioned in the introduction, I will be using a subset of all the movies available to us due to limiting computing power available.

#### Movie Description Based Recommender

Let us first try to build a recommender using movie descriptions and taglines. We do not have a quantitative metric to judge our machine's performance so this will have to be done qualitatively.

```python
smd['tagline'] = smd['tagline'].fillna('')
smd['description'] = smd['overview'] + smd['tagline']
smd['description'] = smd['description'].fillna('')

tf = TfidfVectorizer(analyzer='word', ngram_range=(1, 2), min_df=0, stop_words='english')
tfidf_matrix = tf.fit_transform(smd['description'])
```

#### Cosine Similarity

```Python
cosine_sim = linear_kernel(tfidf_matrix, tfidf_matrix)
cosine_sim[0]
array([1.        , 0.00680476, 0.        , ..., 0.        , 0.00344913,\n       0.        ])
```

We now have a pairwise cosine similarity matrix for all the movies in our dataset. The next step is to write a function that returns the 30 most similar movies based on the cosine similarity score.

```python
def get_recommendations(title):
  	idx = indices[title]
    sim_scores = list(enumerate(cosine_sim[idx]))
    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)
    sim_scores = sim_scores[1:31]
    movie_indices = [i[0] for i in sim_scores]
    return titles.iloc[movie_indices]
```

We're all set. Let us now try and get the top recommendations for a few movies and see how good the recommendations are.

## Conclusion

* The 2 ways of building the engine are capable but the Content Based Recommende, proof to be more accurate than just the Simple Recommende.
* This is an easy way of approaching a Netflix recommendation engine throught Python code and easy to implement.
* What are the next steps?
  - Get the GUI to be fully operated.
  - Connect to a Netflix API to be able to replicate this with new and versatile input.
  - Get the Maps feature working to set the Cinema Geolocalozation.
  - To built and App that englobe all this features.






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

