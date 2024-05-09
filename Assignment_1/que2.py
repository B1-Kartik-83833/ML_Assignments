import pandas as pd


def function():
    #i) Read the dataset "Advertising.csv" in data frame.
    df = pd.read_csv('./Advertising.csv')
    print(df)
    #ii) Print first five records of dataset.
    print(f"first 5 records:{df.head(5)}")
    #iii) print last five records from dataset.
    print(f"last five records {df.tail(5)}")
    #iv)  display the column names of the dataset.
    print(f"coloums names:{df.columns}")
    #v) display last three records from dataset.
    print(f"last three records {df.tail(3)}")
    #vi) display the information about the dataset and analyse the data.
    df.info()
    print(df.describe())
    #vii) display data types of each columns.
    # print(df['TV'])
    print(df.dtypes)
    print(80 * '-')
    #viii)check for null values in the dataset and display the sum of null values inside the column.
    print(df.isna().sum())
    #ix) drop all null values.
    df.dropna(axis=0, inplace=True)
    print(df.isna().sum())
    #x) drop a column 'radio' from a dataset and display first ten records.
    print(df.drop('radio', axis=1, inplace=True))

    print(df.head(10))
    #xi) increase the sales by 10% and add a new column "updated_sales" in dataframe.
    df['Updated_Salary'] = df['sales'] * 0.10
    print(df)
    #xii) display shape of data.
    print(df.shape)


function()
