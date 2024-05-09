import pandas as pd


def function():
    df = pd.read_csv('./Salaries .csv')
    #ii) display first five records.
    print(df.head(5))
    #iii) display first ten records.
    print(df.head(10))
    #iv) display last five records.
    print(df.tail(5))
    #v) display last ten records
    print(df.tail(10))
    #vi) display the columns inside the dataset.
    print(df.columns)
    #vii) display shape of data.
    print(df.shape)
    #viii)describe the dataset
    print(df.describe())


function()
