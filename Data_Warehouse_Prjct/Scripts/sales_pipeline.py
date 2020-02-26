import pandas as pd

def extract(file_name):
    global df
    df = pd.read_csv(file_name)
    return df

def transform():
    df.CustomerID.fillna(value=0, inplace=True)
    df.CustomerID = df.CustomerID.astype(int)
    df.Description = df.Description.str.replace(r',' , ' ')
    return df


def load(export_name):
    df.to_csv('{}.csv'.format(export_name))



if __name__ == "__main__":
    file_name = 'Online-Retail.csv'
    export_name = 'Retail_S3'
    extract(file_name)
    transform()
    load(export_name)
