### DROP COLUMNS FORM A DATASET

cols_to_remove = ['id', 'Date', 'living area', 'lot area']
cols_to_remove = [col for col in cols_to_remove if col in df.columns]
df2 = df.drop(cols_to_remove, axis=1)



