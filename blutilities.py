"""
@Fish Wang

"""

import psycopg2
import pandas as pd

import strategy

import matplotlib.pyplot as plt

from blbbands import plot_data,bollinger_bands


class myStrategy(strategy.Strategy):

    def __init__(self,):

        pass


    def handle_data(self):
        pass






# - import data from sql

def get_data(stock):

    conn = psycopg2.connect("dbname = 'ashare'")
    sql = "SELECT * FROM yahoo_data WHERE code = '%s'" % stock

    df = pd.read_sql(sql, conn)

    conn.close()

    df.set_index("Date",inplace = True)

    # print upper

    return df

# - plot data


# standards/ indicators
# - Bollinger bands
# - MA



def test():

    df = get_data("000099")

    df["upper"],df["lower"]= bollinger_bands(df["Adj Close"], 20)

    #plot_data(df,20)

    d = myStrategy()

    fig , axs = plt.subplots(2,sharex = True)

    df[["upper","lower","Adj Close"]].plot(title ="Stock Prices",ax =axs[0])
    (df["Volume"]/1000000).plot(title = "Volume",ax =axs[1])
    plt.Figure(figsize=(15,15))

    plt.show()


    print df['2016-01-01':].head()
    print "passed ..."



if __name__ == "__main__":

    test()