import pandas as pd
import numpy as np
import tensorflow as tf
#           Data working
#_________________________________________________


train_df = pd.read_csv("train.csv",low_memory=False)
test_df = pd.read_csv("test.csv",low_memory=False)

#removes unnessesery collums
train_df.pop("id")
test_df.pop("id")

#copy datadram into the correct datavar
train_x = train_df.copy()
test_x = test_df.copy()

#puts the output we want into seperate datavar
train_y = train_x.pop("satisfaction")
test_y = test_x.pop("satisfaction")

#-----------------------------------------------------------

head = True
describe = False
shape = False

if head == True:
    print(train_x.head())

if describe == True:
    print(train_x.describe())

#------------------------------------------------------------




#_________________________________________________


#_________________________________________________


#_________________________________________________

#_________________________________________________


#_________________________________________________


#_________________________________________________


#_________________________________________________
