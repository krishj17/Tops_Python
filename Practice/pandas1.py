# Pandas : Built on top of NumPy.
# Designed for data manipulation and analysis.
# Provides Dataframe to store data in rows and columns.
# Makes it easy to clean, filter, reshape, and merge data.


import pandas as pd

data = {
    "Name": ["Harsh", "Mohit", "Rohit"],
    "Age": [23, 25, 21]
}
df = pd.DataFrame(data)   # Dict to DataFrame
print(df)

# View data:--
print("Head: \n", df.head(2))   
print("Tail: \n", df.tail(2))    
print("Describe: \n", df.describe())# Stats summary (mean, std, min, max)

# Select Particular data:--
print("Selection:----- \n", df["Name"])       
print("iloc:----- \n", df.iloc[0])          
print("loc:----- \n", df.loc[0, "Name"])    
print("Age>22:----- \n", df[df["Age"] > 22])  