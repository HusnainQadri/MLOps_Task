import pandas as pd
from sklearn.linear_model import LinearRegression
import pickle

data = pd.read_csv('Salary_Data.csv')

X = data.iloc[:, :-1].values
y = data.iloc[:, 1].values

model = LinearRegression()

model.fit(X, y)

filename = 'linear_regression_model.pkl'
with open(filename, 'wb') as file:
    pickle.dump(model, file)
