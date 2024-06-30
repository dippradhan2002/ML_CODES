##########################################################
#            Date Validation
##########################################################


def validate_datetime_column(df, column_name, date_format='%Y-%m-%d'):
    errors = []
    if not pd.api.types.is_datetime64_any_dtype(df[column_name]):
        errors.append(f"Data type check failed for column '{column_name}'. Expected datetime.")
    try:
        pd.to_datetime(df[column_name], format=date_format, errors='raise')
    except (TypeError, ValueError):
        errors.append(f"Format validation failed for column '{column_name}'. Expected format: {date_format}.")
    if df[column_name].isnull().any():
        errors.append(f"Presence check failed for column '{column_name}'. Null values are not allowed.")

    return errors


##########################################################


# Validate 'datetime_column'
datetime_validation_errors = validate_datetime_column(df, 'datetime_column', date_format='%Y-%m-%d')

# the above will return all the errors


