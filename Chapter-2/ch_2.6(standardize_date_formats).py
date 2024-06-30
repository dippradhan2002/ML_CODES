# DIFFERENT KIND OF DATE FORMAT MAYBE PRESENT,HOW TO HANDLE THEM ?
##########################################################################################################################
            '2020-01-01',        # Standard YYYY-MM-DD
            '2020/02/02',        # Different separator
            '03-03-2020',        # DD-MM-YYYY
            'April 4, 2020',     # Month name and comma
            '2020.05.05',        # Different separator
            '2020-01-01 12:30',  # Date and time
            '2020-12-25T15:30:00Z',  # ISO 8601 format
            '2023-Mar-15',       # Month abbreviation
            '10th September 2021',  # Ordinal number in day
            '2022-Feb-30',       # Invalid date
            '2021-04-31',        # Invalid date
            '2020-06-17T10:30:00-05:00',  # ISO 8601 format with timezone
            'May 1st, 2019',     # Month name with ordinal number in day
            '23rd of June, 2018',  # Ordinal number in day with month name
            'Saturday, 5th of December, 2020'  # Weekday with full date
##########################################################################################################################


# Install python-dateutil Library (It will convert all sort of date format into a valid format,if invalid date is there fillup with NaN)
pip install python-dateutil

# Import parser library
from dateutil import parser

# Function to make all date and time in a correct format
def standardize_date_formats(df, column_name):
    def parse_and_format_date(date_str):
        try:
            dt = parser.parse(date_str)
            return dt.strftime('%Y-%m-%d')
        except (parser.ParserError, ValueError):
            return np.nan  # Fill invalid dates with np.nan

    df[column_name] = df[column_name].apply(parse_and_format_date)
    return df

# Implementation of this function
df_cleaned = standardize_date_formats(df, 'date_column')
