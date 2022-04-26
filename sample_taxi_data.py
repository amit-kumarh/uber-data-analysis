import pandas as pd

def sample(date):
    print('Reading Green')
    green = pd.read_csv(f'taxi_data/green{date}.csv')
    print('Reading Yellow')
    yellow = pd.read_csv(f'taxi_data/yellow{date}.csv')
    print('Concatenating and Sampling')
    new = pd.concat([green.sample(frac=.05), yellow.sample(frac=.05)]).reset_index(drop=True)
    new['VendorID'] = new['VendorID'].astype(str)
    print('Writing')
    new.to_feather(f'taxi_data/{date}.feather')

sample('415')
