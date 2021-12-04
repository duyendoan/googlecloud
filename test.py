import pandas as pd
pd.set_option('display.max_colwidth', None)
#from sklearn.feature_extraction.text import CountVectorizer, TfidfVectorizer
import matplotlib.pyplot as plt
import scipy.spatial.distance as dist
import numpy as np
from dask import dataframe as dd
import timeit


def get_movies():
    url = 'https://drive.google.com/file/d/1WRAizHFm1UjxXEusUK4506QIffLkRzlJ/view?usp=sharing'
    file_id=url.split('/')[-2]
    dwn_url='https://drive.google.com/uc?id=' + file_id
    df = pd.read_csv(dwn_url)
    return df.to_json()

def get_movies_by_id(id):
    url = 'https://drive.google.com/file/d/1WRAizHFm1UjxXEusUK4506QIffLkRzlJ/view?usp=sharing'
    file_id=url.split('/')[-2]
    dwn_url='https://drive.google.com/uc?id=' + file_id
    df = pd.read_csv(dwn_url)
    return df[df.movieId == id].to_json()

def get_movies_by_movieId_userId(movieId, imdbId):
    url = 'https://drive.google.com/file/d/1WRAizHFm1UjxXEusUK4506QIffLkRzlJ/view?usp=sharing'
    file_id=url.split('/')[-2]
    dwn_url='https://drive.google.com/uc?id=' + file_id
    df = pd.read_csv(dwn_url)
    return df[(df.movieId == movieId) & (df.imdbId == imdbId)].to_json()