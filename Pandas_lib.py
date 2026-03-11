
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

      #Numpy library





