# Explore the dataset


#check the shape of the dataset
df.shape

# Get information about the dataset
print(df.info())

# Display the first few rows of the dataset
print(df.head())

# Display the last few rows of the dataset
print(df.tail())

# Display random 3 rows of the dataset
print(df.sample(3))

#in the above two process we may not see all the rows and columns so better to do as below
pd.set_option('display.max_columns',None)
pd.set_option('display.max_rows',None)
print(df)

# Check for missing values
print(df.isnull().sum()) #visible for each columns (returns how many trues are there in the particular column)

# Check for missing values(in the whole dataset)
print(df.isnull().sum().sum())

# Value count (gives all the class values of a column)
df['city'].value_counts()
