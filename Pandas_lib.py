
        #  pandas

         #DataFrames data structure
# import pandas as pd

# mydataset={
#     'cars':["BMW", "PORCHE", "FORD"],
#     'engine':[6, 3, 16]
# }

# myvar = pd.DataFrame(mydataset)
# print(myvar)

            # Pandas Series data structure

# import pandas as pd

# a = [10,12,13]

# myvar = pd.Series(a)
# print(myvar)


        #Data Cleaning

# (Pandas - Cleaning Empty Cells)

# import pandas as pd  

# df=pd.read_csv('data.csv')
# new_df = df.dropna()
# print(new_df.to_string()).


# Pandas - Cleaning Data of Wrong Format

# import pandas as pd

# df=pd.read_csv('data.csv')
# df['Date'] = pd.to_datetime(df['Date'], format='mixed')

# print(df.to_string())   

# Pandas - Fixing Wrong Data

# import pandas as pd

# df = pd.read_csv('data.csv')

# print(df.duplicated())


# from dictionary

# import pandas as pd

# df = pd.DataFrame({
#     "product" : ["pen","book"],
#     "price" : [40,50]
# })
# print(df)

# from list
# import pandas as pd

# data = [["jigar",22],["niket",30]]
# df = pd.DataFrame(data,columns=["name","age"])

# print(df)

import pandas as pd

data = {
    "Name":["Niket","Jigar","Bhavin","Sandeep","poojan","Jenish"],
    "Hobby":["chess","cricket","coding","racing","writing","hacking"],
    "Age":[22,21,23,21,22,25]
}
df=pd.DataFrame(data)

# print(df.head())  #showing first 5 rows
# print(df.tail())    #showing last 5 rows
# print(df.info())     #show structure
# print(df.describe())  #show statistics

# print(df["Name"]) #show only name column
# print(df[["Name","Age"]])  #show multipal columns
# print(df.loc[0]) #showing the specific index value

# print(df["Age"]<23)  #showing values smaller the 23
# print(df[(df["Age"] <=23) & (df["Name"] == "Bhavin")])   #multiple comaprison with data
# print(df[(df["Age"] < 23) & (df["Hobby"] == "cricket")])  #multiple comaprison with data

# df["Salary"] = [30000,40000,50000,60000,80000,40000]  #adding the new column
# print(df)

# df["Total"] = df["Age"] * df["Salary"]    
# print(df)

# df.loc[0,"Age"] = 25   #updating the value
# print(df)

# print(df.drop("Age", axis=1))  # deleting the column if axis=1

# print(df.drop(0))   #deleting the perticular index row




