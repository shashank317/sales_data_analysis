import pandas as pd
# This script reads a CSV file, prints the first 5 rows, shape, columns, data types, and missing values of the dataframe.
# It uses the pandas library to handle the data and the latin1 encoding to read the file.
# The script is useful for data exploration and understanding the structure of the dataset before performing any analysis or cleaning.

df = pd.read_csv("DATASET.csv", encoding = "latin1")
print("First 5 rows : \n", df.head()) # prints the first 5 rows
print("\nShape:", df.shape) #prints the shape of the dataframe
print("\nColumns:\n", df.columns)# prints the columns of the dataframe
print("\nData Types:\n", df.dtypes) # prints the data types of the columns
print("\nMissing Values:\n", df.isnull().sum())# prints the missing values in the dataframe and .sum() gives the sum of missing values

# data loading is done

#Data Clening 
df["Order Date"] = pd.to_datetime(df["Order Date"])
df["Ship Date"] = pd.to_datetime(df["Ship Date"])

df = df.drop_duplicates() # remove duplicates

print("\nAfter removing duplicates, the shape of the dataframe is:", df.shape) # prints the shape of the dataframe after removing duplicates
#df = df.dropna() # remove missing values

df["Renuve after discount"] = df["sales"] *(1 - df["Discount"])
df["Order Month "]= df["Order Date"].df.to_period("M")
df["Shipping Time"] = (df("Ship Date") - df["Order Date"]).dt.days
df["Profit Margin (%)"] = (df["Profit"] / df["Sales"]) * 100


