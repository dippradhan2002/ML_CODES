# Explore the dataset

# Set the value option as below
pd.set_option('display.max_columns',None)
pd.set_option('display.max_rows',None)

#check the shape of the dataset
df.shape

# Get information about the dataset
print(df.info())

# Descriptive statistics (mean, std, min, max, etc.) of numeric columns
df.describe()

# Display the first few rows of the dataset
print(df.head())

# Display the last few rows of the dataset
print(df.tail())

# DViewing the last few rows
df.sample(n)  # Displays n random rows from the dataset

# Check for missing values
print(df.isnull().sum()) 

# Check for missing values of each columns in percentage
df.isnull().sum()/len(df)*100

# Check for missing values(in the whole dataset)
print(df.isnull().sum().sum())

# Counts occurrences of each unique value in 'column_name'
df['column_name'].value_counts()  

# Returns Unique values in a column
df['column_name'].unique()  

# Returns the number of duplicate rows in the dataset
df.duplicated().sum()  

# Returns the Data types of all columns
df.dtypes  

# Correlation matrix (for numeric columns)
df.corr()  # Calculates the correlation between numeric columns

# Sorting values
df.sort_values(by='column_name')  # Sorts the DataFrame by 'column_name'

# Selecting specific columns
df[['column1', 'column2']]  # Selects specific columns 'column1' and 'column2'

# Filtering rows based on conditions
df[df['column_name'] > value]  # Filters rows where 'column_name' is greater than 'value'

# Replacing values
df['column_name'].replace(old_value, new_value)  # Replaces 'old_value' with 'new_value' in 'column_name'










