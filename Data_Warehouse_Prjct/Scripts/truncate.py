import pandas as pd


def truncate(file, trunc):
    df = pd.read_csv(file)
    df = df.head(trunc)
    return df

def export(df, name):
    df.to_csv('{}.csv'.format(name))


if __name__ == '__main__':
    file = 'Online-Retail.csv'
    trunc = 50000
    name = 'Sales_17022020'
    truncate(file, trunc)
    export(df, name)
