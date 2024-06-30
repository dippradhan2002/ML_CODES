def make_feature_names(df):
    df.columns = df.columns.str.replace(' ', '_')
    return df


_________________________________

df_cleaned = make_feature_names(df)
