import pandas as pd

people = {
    "first": ["Corey", 'Jane', 'John'],
    "last": ["Schafer", 'Doe', 'Doe'],
    "email": ["CoreyMSchafer@gmail.com", 'JaneDoe@email.com', 'JohnDoe@email.com']
}
#
# print(type(people))
#
people_df = pd.DataFrame(people)
#
# print(people_df)

countries_df = pd.DataFrame({
'country': ['United States', 'The Netherlands', 'Spain', 'Mexico', 'Australia'],
'capital': ['Washington D.C.', 'Amsterdam', 'Madrid', 'Mexico City', 'Canberra'],
'continent': ['North America', 'Europe', 'Europe', 'North America', 'Australia'],
'language': ['English', 'Dutch', 'Spanish', 'Spanish', 'English']})
#
# print(countries_df)

banks_df = pd.read_csv("top100banks.csv", index_col="rank")
# # Alternatively index can be set via
# # banks_df = banks_df.set_index("rank")
# print(banks_df)
# print(banks_df.head(5)) # first 5 entries
# print(banks_df.tail(20)) # last 20 entries
# print(banks_df.shape) # shape tuple (lines, rows)

# Set countries_df index to country
countries_df = countries_df.set_index("country")


# # Use loc and iloc "query" to get capital of Mexico
# print(countries_df.loc["Mexico", "capital"])
# print(countries_df.iloc[3, 0])
#
#
# # Use loc and iloc "query" to get all languages
# print(countries_df.loc[:, "language"])
# print(countries_df.iloc[:, 2])
#
# # Use loc and iloc "query" to get all data for Spain
# print(countries_df.loc["Spain", :])
# print(countries_df.iloc[2, :])

# # How method columns works
# print(banks_df.columns)
#
# # How columns names can be called
# print(banks_df.bank)
#
# # Calling multiple columns MUST be a list in a list
# print(banks_df[["bank", "country", "total_assets_us_b"]])


# # Using slicing with loc
# print(banks_df.loc[0:4, "bank":"total_assets_us_b"])
#
# # Using slicing with iloc
# print(banks_df.iloc[1:5, 0:3])
#
# # Using list with loc
# print(banks_df.loc[[1, 3, 10], "bank":"total_assets_us_b"])
#
# # Using list with iloc
# print(banks_df.iloc[[1, 3, 10], 0:3])

# # Dataframe vs. string outputs
# print(type(banks_df.iloc[[2], [1]]))
# print(banks_df.iloc[[2], [1]])
# print("*"*10)
# print(type(banks_df.iloc[2,1]))
# print(banks_df.iloc[2,1])
# print("*"*10)
# print(type(banks_df.loc[2, "bank"]))
# print(banks_df.loc[2, "bank"])

# # alternative input using variables for better readability
# rows = [1,2,3,4]
# cols = ["bank", "total_assets_us_b"]
# print(banks_df.loc[rows, cols])

# FILTERING
filt = (banks_df['bank'] == 'Bank of China') & (banks_df['country'] == 'China') # | == AND
print(type(filt))
print(filt)

filt = (banks_df['bank'] == 'Suntrust Banks') | (banks_df['country'] == 'China') # | == OR
print(type(filt))
print(filt)


print(banks_df.loc[filt, ["rank", "total_assets_us_b"]])  # print all under filter
print(40*"*")
print(banks_df.loc[-filt, ["bank", "total_assets_us_b"]]) # printing all NOT in filter


high_rank = (banks_df["rank"] < 15)
print(banks_df.loc[high_rank])
print(banks_df.loc[high_rank,"rank":"country"])

print(banks_df.loc[banks_df["rank"] < 15, :])
print(banks_df.loc[
    (banks_df["rank"] < 15) & (banks_df["country"] != 'China'),
    ['bank'],
      )