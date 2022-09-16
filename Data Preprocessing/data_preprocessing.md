## Importing libraries
```
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
```

---

## Importing dataset
```
dataset = pd.read_csv(path_to_dataset)
```
For this tutorial the dtypes of dataset are
```
Country       object
Age          float64
Salary       float64
Purchased     object
dtype: object
```
---

## Interpolation v/s Imputing

**Interpolation**  
Interpolation (linear) is basically a straight line between two given points where data points between these two are missing. In this case the values that replaces missing nan values can be different.

**Imputation**  
Imputation is filling the missing values with the mean or meadian of the whole column. In this case all the nan values in the column will be replaced by the same value.

### When to choose what?

**Imputation**: If you are given a dataset of patients with a disease (say Pneumonia) and there is a feature called body temperature. So, if there are null values for this feature then you can replace it by average value i.e. Imputation.

**Interpolation**: If you are given a dataset of the share price of a company, you know that every Saturday and Sunday are off. So those are missing values. Now, these values can be filled by the average of Friday value and Monday value i.e. Interpolation.


## Interpolating the missing values
```
#explaining what missing values are and which strategy to use like mean, median
imputer = SimpleImputer(missing_values = np.nan, strategy = "mean")

#fit the model only with the numerical columns to learn the missing values

imputer.fit(X[:,1:3])

# to apply the learnt changes
X[:,1:3] = imputer.transform(X[:,1:3])
```

## Interpolating the missing values
```
dataset["Salary"] = dataset["Salary"].interpolate()
dataset["Age"] = dataset["Age"].interpolate()
X_interpolate = dataset.iloc[:,:-1]
y_interpolate = dataset.iloc[:,-1]
```

---

## Feature Scaling

- Sometimes some features dominate over others as they have large values. Now to get rid of this dominance we scale down the features using normalization or standardization.

**Standardization**  
`x_stand = (x - mean(x))/standard deviation (x)`  
Range : -3 to 3
We can use it in almost every situation.

**Normalization**  
`x_norm = (x - min(x))/(max(x)-min(x))`  
Range = 0 to 1
We use it generally when there is normal distribution between some of the features.

#### Should we apply feature scaling to the dummy variables.
Dummy variables are those that we have created e.g one hot encoded vectors.  
The ans is NO.  
The goal of feature scaling is to bring every feature into the same scale and because the dummy variables are already in the same range we donot need to apply feature scaling.
Also apply feature scaling to the dummy variables might loose its significance  

Note : Use the same scaler model for both train and test set.

---

