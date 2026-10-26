import pandas as pd
bicycle_data = pd.read_csv("bicycle_data.csv")
# Data type: Date - object
# Data type: south of N 34th St total - integer
# Data type: south of N 34th St Cyclist West - integer
# Data type: south of N 34th St Cyclist East - integer

bicycle_data.dtypes
# Notice, the # of sidewalks is a float, when it should be integer

# Drop NAs to remove 
bicycle_data = bicycle_data.dropna()
column_names = bicycle_data.columns.tolist()
bicycle_data[column_names[1:]] = bicycle_data[column_names[1:]].astype(int)
#bicycle_data.iloc[:,1:3] = int(bicycle_data.iloc[:,1:3])
if __name__ == "__main__":
    #print(test_df)
    print(bicycle_data.dtypes)
    