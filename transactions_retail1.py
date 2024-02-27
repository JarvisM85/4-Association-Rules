'''
              Assignment => transactions_retail1.csv
           ============================


'''

'''
Business Objective:

Maximize: 

Minimize: 

ContraintsL: 

'''
'''
DataFrame:

'HANGING'',
'HEART'', 
'HOLDER'', 
'T-LIGHT'', 
'WHITE'', 
'NA'
    

All the columns is of nominal there is no ordinal column in the dataset
'''
import pandas as pd 
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

df1=pd.read_csv('C:/2-Datasets/transactions_retail1.csv')
df1

####################################
df1.columns
'''
[''HANGING'', ''HEART'', ''HOLDER'',
 ''T-LIGHT'', ''WHITE'', 'NA']
'''
###################################
df1.shape
# There is total 557040 rows and 6 columns 
###################################
df1.dtypes
'''
'HANGING'    object
'HEART'      object
'HOLDER'     object
'T-LIGHT'    object
'WHITE'      object
NA           object
dtype: object
'''
# All the data in the dataset is of object type
####################################
df1.info()

'''
 #   Column     Non-Null Count   Dtype 
---  ------     --------------   ----- 
 0   'HANGING'  557040 non-null  object
 1   'HEART'    538818 non-null  object
 2   'HOLDER'   525799 non-null  object
 3   'T-LIGHT'  436182 non-null  object
 4   'WHITE'    222350 non-null  object
 5   NA         83150 non-null   object
dtypes: object(6)


'''
###################################################
a=df1.describe()
a

'''
Out[65]: 
       'HANGING'  'HEART' 'HOLDER' 'T-LIGHT' 'WHITE'     NA
count     557040   538818   525799    436182  222350  83150
unique       949     1177     1099       856     489    184
top        'BAG'  'HEART'    'RED'      'OF'   'SET'  'SET'
freq       41795    16186    18724     20683   14738  16194
'''

##################################################################

# Check for the null values
v=df1.isnull()
v.sum()

'''
'HANGING'         0
'HEART'       18222
'HOLDER'      31241
'T-LIGHT'    120858
'WHITE'      334690
NA           473890
dtype: int64
'''

##############################################

b=pd.isnull(df1)
b.sum()

'''
'HANGING'         0
'HEART'       18222
'HOLDER'      31241
'T-LIGHT'    120858
'WHITE'      334690
NA           473890
dtype: int64
'''

################################################

# Five Number Summary
v=df1.describe()
# The mean value is near to zero and also the standard deviation is a;dp
# near to zero and the meadian value for the all datapoints is zero
df1.info()

'''
#   Column     Non-Null Count   Dtype 
---  ------     --------------   ----- 
 0   'HANGING'  557040 non-null  object
 1   'HEART'    538818 non-null  object
 2   'HOLDER'   525799 non-null  object
 3   'T-LIGHT'  436182 non-null  object
 4   'WHITE'    222350 non-null  object
 5   NA         83150 non-null   object
dtypes: object(6)
'''

################################################
# This will give us the informationn about all the points

####################################
# Visualization of Data

# 1. Check for the outlier

sns.boxplot(df1,x='HANGING')
# No outlier 
sns.boxplot(df1,x='YouthBks')
#There is one outlier 
sns.boxplot(df1,x='HOLDER')
# No Outlier
sns.boxplot(df1,x='WHITE')
# There is one outlier
sns.boxplot(df1)


