### install klib library in the system ( https://pypi.org/project/klib/ )
pip install klib

## Usage
import klib
import pandas as pd

df = pd.DataFrame(data)


# klib.clean - functions for cleaning datasets
klib.mv_col_handling(df) # drops features with high ratio of missing vals based on informational content


klib.data_cleaning(df) # performs datacleaning (drop duplicates & empty rows/cols, adjust dtypes,...)
****************************************************************************************************
# THE BELOW THREE FUNCTIONS ARE ALREADY DEFINED INSIDE data_cleaning()
****************************************************************************************************
klib.clean_column_names(df) # cleans and standardizes column names, also called inside data_cleaning()
klib.convert_datatypes(df) # converts existing to more efficient dtypes, also called inside data_cleaning()
klib.drop_missing(df) # drops missing values, also called in data_cleaning()
****************************************************************************************************

# klib.describe - functions for visualizing datasets
klib.cat_plot(df) # returns a visualization of the number and frequency of categorical features
klib.corr_mat(df) # returns a color-encoded correlation matrix
klib.corr_plot(df) # returns a color-encoded heatmap, ideal for correlations
klib.corr_interactive_plot(df, split="neg").show() # returns an interactive correlation plot using plotly
klib.dist_plot(df) # returns a distribution plot for every numeric feature
klib.missingval_plot(df) # returns a figure containing information about missing values
