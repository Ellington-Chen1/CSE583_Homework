import pandas as pd
bicycle_data = pd.read_csv("bicycle_data.csv")
# Data type: Date - datetime
# Data type: south of N 34th St total - integer
# Data type: south of N 34th St Cyclist West - integer
# Data type: south of N 34th St Cyclist East - integer

bicycle_data.dtypes
# Notice, the # of sidewalks is a float, when it should be integer

# Drop NAs to remove 
bicycle_data = bicycle_data.dropna()
# Pull list of column names
column_names = bicycle_data.columns.tolist()
# Convert columns on interest from float to int
bicycle_data[column_names[1:]] = bicycle_data[column_names[1:]].astype(int)
# Convert date column to panda datatime format for easy of pulling date/time
bicycle_data["Date"] = pd.to_datetime(bicycle_data["Date"])

# Add total column (already exists???) by summing columns 3 and 4
bicycle_data["Total"] = bicycle_data[column_names[2:]].sum(axis = 1)

if __name__ == "__main__":
    print(bicycle_data["Date"].dt.hour)
    