#! /usr/bin/python3

# import pandas library
import pandas as pd

# URL of online data
url = "https://s3-api.us-geo.objectstorage.softlayer.net/cf-courses-data/CognitiveClass/DA0101EN/auto.csv"

# Read the online file and assign it to variable "df"
print("\n\nLoading data from:\n",url)
df = pd.read_csv(url, header=None)

# show the first 5 rows using dataframe.head() method
print("\n\nThe first 5 rows of the dataframe:\n",df.head(5))

# show the bottom 10 rows of data frame
print("\n\nThe last 10 rows of the dataframe:\n",df.tail(10))

print("-"*80)
input("Press Enter to continue...")

# create headers list
headers = [ "symboling",
            "normalized-losses",
            "make",
            "fuel-type",
            "aspiration",
            "num-of-doors",
            "body-style",
            "drive-wheels",
            "engine-location",
            "wheel-base",
            "length",
            "width",
            "height",
            "curb-weight",
            "engine-type",
            "num-of-cylinders",
            "engine-size",
            "fuel-system",
            "bore",
            "stroke",
            "compression-ratio",
            "horsepower",
            "peak-rpm",
            "city-mpg",
            "highway-mpg",
            "price"
        ]

print("\n\nAdding headers:\n\n", headers)

#  We replace headers and recheck our data frame
df.columns = headers
print("-"*80)
input("Press Enter to continue...")

# show the first 5 rows using dataframe.head() method
print("\n\nThe first 5 rows of the dataframe\n",df.head(5))
print("-"*80)
input("Press Enter to continue...")



print("\n\nColumns :\n", df.columns)
print("-"*80)
input("Press Enter to continue...")

# Data Types
print("\n\nData types:\n",df.dtypes)
print("-"*80)
input("Press Enter to continue...")

# describe numrical columns 
print("\n\nData Frame Describe:\n",df.describe())
print("-"*80)
input("Press Enter to continue...")

# we can drop missing values along the column "price" as follows  
print("\n\nDrop rows which contain missing values in column \"price\":\n")
df2=df.dropna(subset=["price"], axis=0)
print(df2.describe())

#Save Dataset
file_name = "data/automobile.csv"
print("\n\nSaving data set to",file_name,"\n")
df.to_csv(file_name, index=False)

print("-"*80)
input("Press Enter to continue...")

#  Data Formate  | Read           | Save      
#  ------------- |:--------------:| ----------
#  csv           | pd.read_csv()  | df.to_csv()
#  json          | pd.read_json() | df.to_json()
#  excel         | pd.read_excel()| df.to_excel()
#  hdf           | pd.read_hdf()  | df.to_hdf()
#  sql           | pd.read_sql()  | df.to_sql()

# describe all the columns in "df" 
print("\n\nData Frame Describe All:\n",df.describe(include = "all"))
print("-"*80)
input("Press Enter to continue...")

# describe some columns
print("\n\nData Frame Describe 2 selected columns:\n",df[['length', 'compression-ratio']].describe())
print("-"*80)
input("Press Enter to continue...")

# dataframe info
print("\n\nData Frame info:\n",df.info)

