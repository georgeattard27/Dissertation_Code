# -*- coding: utf-8 -*-
"""
Created on Mon Apr 17 17:56:49 2023

@author: georg
"""

import os
from datetime import datetime
import re
import pandas
import numpy as np


path = os.getcwd()
os.chdir(path)
recipes_df = pandas.read_csv('recipes.csv')


# Removing unnecessary columns
del recipes_df['CookTime']
del recipes_df["PrepTime"]
del recipes_df['TotalTime']
del recipes_df['DatePublished']
del recipes_df['Description']
del recipes_df["Images"]
del recipes_df['Keywords']
del recipes_df['RecipeIngredientQuantities']
del recipes_df['AggregatedRating']
del recipes_df['ReviewCount']
del recipes_df['SaturatedFatContent']
del recipes_df['CholesterolContent']
del recipes_df['CarbohydrateContent']
del recipes_df['RecipeYield']
del recipes_df['RecipeInstructions']


# Removing Recipe ID duplicates
recipes_df.drop_duplicates(subset='RecipeId', keep='first', inplace = True, ignore_index=True)

# Removing rows with a weblink in most of the row fields "https://..."
stringtodiscard = "https://"
index_list = recipes_df.index.tolist()
droplist = [index for index in index_list if str(recipes_df['RecipeId'][index]).find(stringtodiscard) != -1]
recipes_df.drop(droplist, inplace = True)
recipes_df.reset_index(drop = True, inplace = True)

#Changing AuthorName column into str
recipes_df['AuthorName'] = recipes_df.AuthorName.astype(str)

#Reviews
reviews_df = pandas.read_csv("reviews.csv")

# Removing unnecessary columns
del reviews_df['ReviewId']
del reviews_df['Review']
del reviews_df['DateSubmitted']
del reviews_df['DateModified']

#Checking that the RecipeId from the reviews_df exists in the recipes_df
index_list = reviews_df.index.tolist()
droplist1 = [index for index in index_list if reviews_df['RecipeId'][index] not in recipes_df['RecipeId'].values]
reviews_df.drop(droplist1, inplace = True)
reviews_df.reset_index(drop = True, inplace = True)

#Exporting back to *.csv files
recipes_df.to_csv('recipes_afterStep1a.csv')
reviews_df.to_csv('reviews_afterStep1a.csv')