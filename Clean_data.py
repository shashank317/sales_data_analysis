import pandas as pd
df = pd.read_csv("DATASET.csv", encoding = "latin1")
print("First 5 rows : \n", df.head()) # prints the first 5 rows
print("\nShape:", df.shape) #prints the shape of the dataframe
print("\nColumns:\n", df.columns)# prints the columns of the dataframe
print("\nData Types:\n", df.dtypes) # prints the data types of the columns
print("\nMissing Values:\n", df.isnull().sum())# prints the missing values in the dataframe and .sum() gives the sum of missing values