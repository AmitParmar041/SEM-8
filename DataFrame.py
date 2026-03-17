import pandas as pd

data = {

    "Id":[1,2,3,4,5,6,7,8,9,10],
    "Dob":["21-02-2004","20-03-2004","10-03-2006","12-04-2008","23-03-2009","30-12-2011","01-01-2025","23-08-2022","31-07-2018","05-03-2001"],
    "Age":[25,30,25,25,45,21,23,25,54,52],
    "Name":["Bhavin","Niket","Sandeep","Poojan","Denny","Joe","Baki","Yujiro","Ramesh","Suresh"],
    "Roll_no":[21,22,23,24,25,26,27,28,29,30],
    "Gender":["Male","Male","Male","Male","Male","Male","Male","Male","Male","Male"],
    "Phone_Number":[9865986598,9865875487,8754875487,5465986598,8754876598,6532655488,9865548798,9865325421,6598658754,9865875487],
    "SCI":[54,98,65,54,87,65,32,None,87,54],
    "Computer":[65,87,54,None,65,32,54,65,21,54],
    "Maths":[65,None,54,65,32,54,87,65,21,65],
    "SS":[98,65,87,None,87,54,65,32,54,95],
    "Total":[234,236,321,213,123,234,287,360,256,251],
    "Percentage":["80%","92%","64%","87%","86%","51%","32%","82%","56%","60%"],
    "Grade":["A+","C+","B+","A+","B+","P","C+","O","A+","B+"],

}

df = pd.DataFrame(data)
# print("Mean")
# print(df["SCI"].mean())
# print(df["Computer"].mean())
# print(df["Maths"].mean())
# print(df["SS"].mean())
# print(df["Total"].mean())
# print("-------------------")
# print("Median")
# print(df["SCI"].median())
# print(df["Computer"].median())
# print(df["Maths"].median())
# print(df["SS"].median())
# print(df["Total"].median())

# print("-------------------")
# print("mode")

# print(df["SCI"].mode())
# print(df["Computer"].mode())
# print(df["Maths"].mode())
# print(df["SS"].mode())
# print(df["Total"].mode())


# print(df["SCI"].isnull)

# print(df["SCI"].duplicated())

# v=df["SCI"].mean()
# print(df["SCI"].fillna(v))

# print(df["SCI"].head())
# print(df["SCI"].tail())
# print(df["SCI"].info())
# print(df["SCI"].describe())

# print(df[df["Age"] > 20])   #single condition
# print(df[df["Age"] < 20])

# print(df[(df["Age"] > 20) & (df["Grade"] == "A+")])  #multipal conditions


# df.loc[0,"SCI"] = 50
# print(df)

# print(df.drop(0))

# print(df.sort_values("Age"))   #printing values in ascending order
# print(df.sort_values("Age",ascending=False))   #printing values in decending order

# print(df["SCI"].sum())
# print(df["SCI"].count())
# print(df["SCI"].max())
# print(df["SCI"].min())
