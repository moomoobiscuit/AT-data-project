import numpy as np
import pandas as pd
import os

# define a function that cleans the data such that we only get columns that have non-null values
def clean_null(fname): 

    # read in the data
    df = pd.read_csv(fname)

    # summarise the data by count
    column_counts = df.describe(include = 'all').transpose()['count']

    # drop columns that are completely empty (zero non-null values)
    df = df.loc[:, column_counts != 0]

    # write to a cleaned csv directory
    if not os.path.exists('data/csv_cleaned'):
        os.makedirs('data/csv_cleaned')
    df.to_csv(
        'data/csv_cleaned/' + os.path.split(fname)[1],
        index = False
    )

for fname in os.listdir('data/csv'):
    clean_null('data/csv/' + fname)