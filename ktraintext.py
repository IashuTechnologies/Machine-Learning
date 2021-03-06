# -*- coding: utf-8 -*-
"""ktraintext.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1eUX0vOh6LU58rY4GlUoMfvxJCTGiqIAM
"""

import pandas as pd

from google.colab import drive 
drive.mount('/content/gdrive')

import pandas as pd 
df=pd.read_csv('gdrive/My Drive/ITSM/text classification/all_tickets.csv')

path='gdrive/My Drive/ITSM/text classification/all_tickets.csv'

!pip3 install ktrain

import os.path
import numpy as np
import tensorflow as tf
import ktrain
from ktrain import text

df=df.dropna()

df.head()

df=df[['body','category']]

df.head()

from sklearn.model_selection import train_test_split

# Use 80% for training and 20% for validation.
x_train, x_test, y_train, y_test = train_test_split(df.body, df.category, 
                                                            random_state=2018, test_size=0.2)

classy=pd.DataFrame(y_train)

y_train=pd.DataFrame(y_train)

y_train.head()

y_train['category'].value_counts()

x_train=pd.DataFrame(x_train)
y_train=pd.DataFrame(y_train)
x_test=pd.DataFrame(x_test)
y_test=pd.DataFrame(y_test)

ydf_train=pd.DataFrame(y_train)

x_train.head()

x_train = x_train.body
y_train = y_train.category
x_test = x_test.body
y_test = y_test.category

(x_train,  y_train), (x_test, y_test), preproc = text.texts_from_csv(train_filepath=path,text_column='body',label_columns='category',preprocess_mode='bert',
                                                                       maxlen=350, 
                                                                       max_features=35000
                                                                       )

model = text.text_classifier('bert', train_data=(x_train, y_train), preproc=preproc)
learner = ktrain.get_learner(model, train_data=(x_train, y_train), batch_size=6)

learner.fit_onecycle(2e-5, 3)

learner.validate(val_data=(x_test, y_test), class_names=[0,1,2,3,4,5,6,7,8,9])

predictor = ktrain.get_predictor(learner.model, preproc)

# let's save the predictor for later use
predictor.save(fpath=F"gdrive/My Drive/ITSM/text classification/model/my_predictorbert")

# reload the predictor
reloaded_predictor = ktrain.load_predictor(fpath=F"gdrive/My Drive/ITSM/text classification/model/my_predictorbert")

# make a prediction on the same document to verify it still works
reloaded_predictor.predict("purachase")

