##########################################################

##########################################################



def validate_categorical_column(df, column_name, allowed_values=None):
    errors = []
    
    if not pd.api.types.is_string_dtype(df[column_name]):
        errors.append(f"Data type check failed for column '{column_name}'. Expected string (categorical).")
    if df[column_name].nunique() != len(df[column_name]):
        errors.append(f"Unique values check failed for column '{column_name}'. All values must be unique.")
    if df[column_name].isnull().any():
        errors.append(f"Presence check failed for column '{column_name}'. Null values are not allowed.")
    if allowed_values is not None and not df[column_name].isin(allowed_values).all():
        errors.append(f"Specific value check failed for column '{column_name}'. Allowed values are {allowed_values}.")
    if not errors:
        return "Validation successful. No errors found."
    else:
        return errors



##########################################################


# Validate 'category_column'
category_validation_errors = validate_categorical_column(df, 'category_column', allowed_values=['Asf', 'Books', 'Cat'])

# the above will return all the errors

