import pandas as pd
import numpy as np
bicycle_data = pd.read_csv("bicycle_data.csv")
# Data type: Date - datetime
# Data type: south of N 34th St total - integer
# Data type: south of N 34th St Cyclist West - integer
# Data type: south of N 34th St Cyclist East - integer

bicycle_data.dtypes
# Notice, the # of sidewalks is a float, when it should be integer

# Pull list of column names
column_names = bicycle_data.columns.tolist()
# Convert columns 2-4 to integer type
bicycle_data[column_names[1:]] = bicycle_data[column_names[1:]].astype("Int64")
# Convert date column to panda datatime format for easy of pulling date/time
bicycle_data["Date"] = pd.to_datetime(bicycle_data["Date"], format="%m/%d/%Y %H:%M:%S %p")

# Add total column (already exists???) by summing columns 3 and 4
bicycle_data["Total"] = bicycle_data[column_names[2:]].sum(axis = 1)
# Pull hour from the date in military format
bicycle_data["Military_Hour"] = bicycle_data["Date"].dt.hour
# Pull year from date
bicycle_data["Year"] = bicycle_data["Date"].dt.year

# Subset the year 2016 into a new df
bicycle_data_2016 = bicycle_data.filter(pd.col('Year') == 2016)

# Found no missing data across the 2016 dataset?
bicycle_data[bicycle_data.isna().all(axis=1)]

if __name__ == "__main__":
    print(bicycle_data[bicycle_data.isna().all(axis=1)])