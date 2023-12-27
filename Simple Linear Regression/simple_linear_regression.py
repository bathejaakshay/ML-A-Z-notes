#Linear Regression is useful when there is a linear relationship between the features and target data.
#Simple linear regression is one in which we just have one feature.

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import accuracy_score
from sklearn.metrics import precision_recall_fscore_support
from sklearn.metrics import mean_squared_error, mean_absolute_error
#import dataset

dataset = pd.read_csv(r"/Users/akshaybatheja/Documents/workspace/Self_learning/ML/Machine Learning A-Z (Codes and Datasets)/Part 2 - Regression/Section 4 - Simple Linear Regression/Python/Salary_Data.csv")
X = dataset.iloc[:,:-1].values
y = dataset.iloc[:,-1].values
X_train, X_test, y_train, y_test = train_test_split(X,y,shuffle=True,test_size=0.2,random_state=0)
regressor = LinearRegression()
regressor.fit(X_train, y_train)

#prediction
y_pred = regressor.predict(X_test)
print(f'mean squared error : {mean_squared_error(y_test, y_pred)}, MAE: {mean_absolute_error(y_test, y_pred)}')

# accuracy metric is used for classification problems. We use MAE, RMSE, MSE, R2score for regression problems.


#regression line plot
plt.scatter(X_test, y_test, color = "blue")
plt.plot(X_train, regressor.predict(X_train), color = "red") # This is a regression line
plt.title('Salary vs Experience (Test set)')
plt.xlabel('Years of Experience')
plt.ylabel('Salary')
plt.show()