##########################################################
#
# Validate a feature column, supose a feature column contains age
# in that case min_value = 0, max_value = 100 (let)
# 
##########################################################


def validate_numeric_column(df, column_name, min_value=None, max_value=None):
    errors = []
    
    if not pd.api.types.is_numeric_dtype(df[column_name]):
        errors.append(f"Data type check failed for column '{column_name}'. Expected numeric.")
    if min_value is not None and (df[column_name] < min_value).any():
        errors.append(f"Range check failed for column '{column_name}'. Minimum value should be {min_value}.")
    if max_value is not None and (df[column_name] > max_value).any():
        errors.append(f"Range check failed for column '{column_name}'. Maximum value should be {max_value}.")
    if df[column_name].isnull().any():
        errors.append(f"Presence check failed for column '{column_name}'. Null values are not allowed.")
    if not errors:
        return "Validation successful. No errors found."
    else:
        return errors



##########################################################


# Validate 'numeric_column'
validation_errors = validate_numeric_column(df, 'numeric_column', min_value=0, max_value=40)

# the above will return all the errors
