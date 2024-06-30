### REPLACE NaN 
****************************************************************************************************
## 1) Rows having `null values` will be deleted
df.replace([np.inf, -np.inf], np.nan, inplace=True)    
df.dropna(inplace=True)
****************************************************************************************************

****************************************************************************************************
****************************************************************************************************
## 2) HANDLE NaN value - some cases some values/string can be put instead of NaN,What to do then ?
  
# 2.1) Removing 9 from the whole dataset to remain with 0 and 1 as yes or no and drop all the rows having NaN values
df.replace(9, np.nan, inplace=True)
df.dropna(inplace=True)
****************************************************************************************************

****************************************************************************************************
# 2.2) Removing 9 from the selected features of a dataset 
# Specify the columns you want to replace 9 with NaN
columns_to_replace = ['A', 'C']
# Replace 9 with NaN only in specified columns
df[columns_to_replace] = df[columns_to_replace].replace(9, np.nan)
****************************************************************************************************

****************************************************************************************************
# 2.3) Removing 9 from the selected features of a dataset
# Specify the columns you want to exclude from replacement
columns_to_exclude = ['B', 'C']
# Create a list of columns to include in the replacement
columns_to_include = df.columns.drop(columns_to_exclude)
# Replace 9 with NaN only in specified columns
df[columns_to_include] = df[columns_to_include].replace(9, np.nan)
****************************************************************************************************
