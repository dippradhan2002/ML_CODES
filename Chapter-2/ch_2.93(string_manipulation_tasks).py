________________________________________
## 1) `Removing Leading/Trailing Whitespaces`
----------------------------------------
# Removing leading/trailing whitespaces
df = df.applymap(str.strip)
________________________________________

________________________________________
# Extract only string parts, ignoring whitespaces and numerics
----------------------------------------
df['cleaned_feature'] = df['feature'].str.replace(r'[^a-zA-Z]', '', regex=True)
________________________________________

________________________________________
`Converting to Lower Case`
----------------------------------------
# Converting all strings to lower case
df = df.applymap(str.lower)
________________________________________

________________________________________
`Converting to Upper Case`
----------------------------------------
# Converting all strings to upper case
df = df.applymap(str.upper)
________________________________________

________________________________________
`Replacing Substrings`
----------------------------------------
# Replacing substrings
df['A'] = df['A'].str.replace('hello', 'hi')
________________________________________

________________________________________
`Extracting Substrings`
----------------------------------------
# Extracting substrings
df['first_char'] = df['A'].str[0]  # First character
df['first_three_chars'] = df['A'].str[:3]  # First three characters
________________________________________

________________________________________
`Finding Substrings`
----------------------------------------
# Finding substrings
df['contains_foo'] = df['B'].str.contains('foo')
________________________________________

________________________________________
`Splitting Strings`
----------------------------------------
# Splitting strings
df[['first_word', 'second_word']] = df['A'].str.split(expand=True)
________________________________________

________________________________________
`Concatenating Strings`
----------------------------------------
# Concatenating strings
df['concatenated'] = df['A'] + ' ' + df['B']
________________________________________

________________________________________
`String Length`
----------------------------------------
# Getting string length
df['A_length'] = df['A'].str.len()
________________________________________

________________________________________
`Removing Specific Characters`
----------------------------------------
# Removing specific characters
df['A_no_spaces'] = df['A'].str.replace(' ', '')
________________________________________

________________________________________
`Padding Strings`
----------------------------------------
# Padding strings
df['A_padded'] = df['A'].str.pad(10, side='left', fillchar='*')
________________________________________


________________________________________
`Checking for Alphanumeric Characters`
----------------------------------------
# Checking for alphanumeric characters
df['A_isalnum'] = df['A'].str.isalnum()
________________________________________

________________________________________
`Checking for Alphabetic Characterss`
----------------------------------------
# Checking for alphabetic characters
df['A_isalpha'] = df['A'].str.isalpha()
________________________________________

________________________________________
`Checking for Digit Characters`
----------------------------------------
# Checking for digit characters
df['A_isdigit'] = df['A'].str.isdigit()
________________________________________

________________________________________
`Replacing Using Regular Expressions`
----------------------------------------
# Replacing using regular expressions
df['A_no_digits'] = df['A'].str.replace(r'\d+', '', regex=True)
________________________________________




















