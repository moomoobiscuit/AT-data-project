import numpy as np
import pandas as pd
import os

# clean csv files -  remove all columns that have no data in them
for fname in os.listdir('data/csv'):

    # read in the data
    df = pd.read_csv('data/csv/' + fname)

    # drop columns that are completely empty (zero non-null values)
    df = df.dropna(axis = 1, how = 'all')

    # write to a cleaned csv directory
    if not os.path.exists('data/csv_cleaned'):
        os.makedirs('data/csv_cleaned')

    df.to_csv(
        'data/csv_cleaned/' + fname,
        index = False
    )
