import pandas as pd

data = pd.read_csv("Datasets/housing2.csv")

# select non numeric columns
non_numeric_columns = data.select_dtypes(exclude=['float64', 'int64']).columns

# remove non numeric values
data.drop(non_numeric_columns, axis=1, inplace=True)

# save the cleaned data
data.to_csv("Datasets/housing2_cleaned.csv", index=False)


