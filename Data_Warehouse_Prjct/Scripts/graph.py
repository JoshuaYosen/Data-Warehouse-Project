import pandas as pd
import matplotlib.pyplot as plt
import datetime
import numpy as np


def DataFrame(file_name):
    df = pd.read_csv(file_name, index_col=0)
    print(df.head(10))
    


def sales_per_month(file_name):
    DataFrame(file_name)
    df['Date'] = pd.DatetimeIndex(df['InvoiceDate']).date
    df['Month'] = pd.DatetimeIndex(df['Date']).month
    df_mthsum = df.groupby(['Month']).sum()
    x = ['December-2010','January-2011']
    y = df_mthsum.Quantity.sort_index(ascending=False)

    plt.bar(x, y)
    plt.xlabel('Months')
    plt.ylabel('Units Sold')
    plt.savefig('UnitsSold_per_Month.png')
    return df



def items_sold(file_name):
    DataFrame(file_name)
    df_itemsSold = df.groupby('StockCode')['Quantity'].sum()

    plt.plot(df_itemsSold)
    plt.savefig('ItemsSold.png')




if __name__ == "__main__":
    file_name = 'SalesData_17022020.csv'
    #DataFrame(file_name)
    sales_per_month(file_name)
    items_sold(file_name)
