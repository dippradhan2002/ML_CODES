# DIFFERENT KIND OF TIME FORMAT MAYBE PRESENT,HOW TO HANDLE THEM ?
##########################################################################################################################
            '12:30:45',        # Standard HH:MM:SS
            '13:45',           # HH:MM
            '2:30 PM',         # 12-hour format with AM/PM
            '17:15:30',        # HH:MM:SS in 24-hour format
            '6:45 A.M.',       # 12-hour format with periods
            '20:00',           # HH:MM in 24-hour format
            '11:30 PM',        # 12-hour format with AM/PM
            '3:20:15',         # HH:MM:SS
            '5 PM',            # HH:MM AM/PM
            'Invalid Time',    # Invalid time format
            '16-30-45',        # Invalid time format
##########################################################################################################################


# Install python-dateutil Library (It will convert all sort of time format into a valid format,if invalid date is there fillup with NaN)
pip install python-dateutil
________________________________________________________________

# Import parser library
from dateutil import parser

________________________________________________________________

# Function to make all time in a correct format
def standardize_time_formats(df, column_name):
    def parse_and_format_time(time_str):
        try:
            dt = parser.parse(time_str)
            return dt.strftime('%H:%M:%S')
        except (parser.ParserError, ValueError):
            return np.nan  # Fill invalid times with np.nan

    df[column_name] = df[column_name].apply(parse_and_format_time)
    return df
________________________________________________________________


# Implementation of this function
df_cleaned = standardize_time_formats(df, 'time_column')
