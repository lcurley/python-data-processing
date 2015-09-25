# import PLING data download

import pandas as pd
# from pandas import read_csv

data = pd.read_csv('usercache_PLING_lauren.csv')
# pling = pd.DataFrame(data)

# sort by columns

subID = data.iloc[:,0]
visitID = data.iloc[:,1]
gender = data.iloc[:,4068]
age = data.iloc[:,4069]
demo_ADHD = data.iloc[:,4070:4094]
demo_CBQ = data.iloc[:,4261:4279]

# append all demographic info

# group all behavioral data
beh_CANTAB = data.iloc[:,4094:4120]
beh_CTOPP = data.iloc[:,4318:4333]
beh_TBX = data.iloc[:,4591:4649]
beh_WISC = data.iloc[:,4841:4854]

# append all behavioral info
# beh_comb = pd.append(beh_CANTAB, beh_CTOPP, beh_TBX, beh_WISC)

# group all cortical surface area, thickness and volumne measures
MRI_data = data.iloc[:,20:335]

# group all DTI (FA and MD) data
DTI_data = data.iloc[:,732:816]


# beh_comb.to_csv('beh_data.csv')
gender.to_csv('gender.csv')
MRI_data.to_csv('MRI_data.csv')
DTI_data.to_csv('DTI_data.csv')