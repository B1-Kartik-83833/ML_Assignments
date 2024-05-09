# 1 i) Create a list of empids and names (10 employees).
import pandas as pd


def function1():
    names = ["N1", "N2", "N3", "N4", "N5", "N6", "N7", "N8", "N9", "N10"]
    empids = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    # ii) Convert list into Series.
    s1 = pd.Series(names, index=empids)
    # s2 = pd.Series(empids)
    # iii) Print type of Series.
    print(f"type of Series:{type(s1)}")
    # print(f"type of Series:{type(s2)}")
    # iv) Convert Series into DataFrame.
    df1 = pd.DataFrame(s1)
    # df2 = pd.DataFrame(s2)

    #v)   a) Display all records.
    print(f"Data frame1:{df1}")
    # print(f"Data frame2:{df2}")
    #     b) Display first five records.
    print(f"first 5 record:{df1.head(5)}")
    #     c) Display last five records.
    print(f"last 5 record:{df1.tail(5)}")

    #vi) Save the record in csv file(Myrecord.csv)
    csv_1 = df1.to_csv('MyRecord.csv')
    print(csv_1)


function1()
