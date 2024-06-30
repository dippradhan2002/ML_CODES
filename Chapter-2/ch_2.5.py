import pandas as pd
import re

# Create a DataFrame
data = {'feature_column': ['2 stops', 'non-stop', '3 stops', '1 stop', 'no stops', '5 stops']}
df = pd.DataFrame(data)

# Function to extract integer
def extract_integer(value):
    match = re.search(r'\d+', value)  # Search for one or more digits
    return int(match.group()) if match else None

# Apply the function to the DataFrame
df['extracted_integers'] = df['feature_column'].apply(extract_integer)

# Print the DataFrame to see the result
print(df)

