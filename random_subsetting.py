#script to randomly sample dataset into subsets and create an overlap sample to include for each subset

#load packages
import pandas as pd 
import numpy as np 

####PARAMETERS###
#load data
data_lk = pd.DataFrame(pd.read_csv("data/feedback_data1_LK.csv"))
data_lc = pd.DataFrame(pd.read_csv("data/feedback_data2_LC.csv"))

#drop data that hasn't been coded yet
data_lk = data_lk.dropna()
data_lc = data_lc.dropna()

#for each dataset, create overlap sample for all raters
overlap_lk = data_lk.sample(frac=0.15) #15% of the original random sample
overlap_lk.to_csv("data/overlap_lk.csv")
overlap_lc = data_lc.sample(frac=0.15) #15% of the original random sample
overlap_lc.to_csv("data/overlap_lc.csv")

# subsets = [1,2,3]
# for subset in subsets:
#  	#new dataframe for each subset
#  	b = randsamp.loc[randsamp['subset']== subset]
#  	#add overlap sample to each subset
#  	df = pd.concat([b, overlap])
#  	#drop duplicates
#  	df.drop_duplicates()
#  	df.to_csv('../data/cogs160/subset_%s.csv' %subset)
