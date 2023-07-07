import pandas as pd

iris_data = pd.read_csv('iris.csv')

print("Shape of the data frame: ", iris_data.shape)

print("Data types of the columns:\n", iris_data.dtypes)

print("First 3 rows of the data frame:\n", iris_data.head(3))
