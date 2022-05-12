# week 11 
import pandas as pd
import csv

df = pd.read_csv("week11_flat_file.csv")

df.tail()

df.tail().isnull()

df.isnull().sum()

df.mean()

# filling Nans with the mean
df.fillna(df.mean(), inplace = True)
# check to see if it worked
df.isnull().sum()

# replace hair_color, eye_color, gender

# gender
df['gender'].value_counts()

df['gender'].replace('Male', 'male', inplace = True)

df['gender'].fillna(value = 'female', inplace = True)

# hair_color
df['hair_color'].value_counts()

df['hair_color'].fillna(value = 'brown', inplace = True)

# eye_color
df['eye_color'].value_counts()

df['eye_color'].fillna(value = 'brown', inplace = True)

# is the missing data gone?
df.isnull().sum()
# yes

# part two
df.mean()
df['height'].sum()
df.median()
df.mode()
df.describe()

df['gender'].mode()
df['hair_color'].mode()
df['eye_color'].mode()



