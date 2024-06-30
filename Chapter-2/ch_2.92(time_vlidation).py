##########################################################

##########################################################
# Import library
import re

# Write thw function

def validate_time_format(df, column_name):
    errors = []
    hh_mm_ss_pattern = re.compile(r'^([01]?[0-9]|2[0-3]):([0-5]?[0-9]):([0-5]?[0-9])$')
    hh_mm_ampm_pattern = re.compile(r'^([0]?[1-9]|1[0-2]):([0-5]?[0-9]) [AP]M$', re.IGNORECASE)

    def check_time_format(time_str):
        if hh_mm_ss_pattern.match(time_str):
            return True, '%H:%M:%S'  # HH:MM:SS format
        elif hh_mm_ampm_pattern.match(time_str):
            return True, '%I:%M %p'  # HH:MM AM/PM format
        else:
            return False, None

    def parse_and_format_time(time_str):
        valid_format, format_str = check_time_format(time_str)
        if valid_format:
            try:
                dt = pd.to_datetime(time_str, format=format_str)
                return dt.strftime(format_str)
            except ValueError:
                return np.nan  # Invalid datetime format
        else:
            return np.nan  # Invalid time format
    df[column_name] = df[column_name].apply(parse_and_format_time)

    return df


##########################################################

# Validate 'time_column'
df_cleaned = validate_time_format(df, 'time_column')



