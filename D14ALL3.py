import pandas as pd
from sklearn.preprocessing import LabelEncoder
data = {
    'Transmission': ['Automatic', 'Manual', 'Automatic', 'Manual'],
    'Color': ['Red', 'Blue', 'Green', 'Red']
}
df = pd.DataFrame(data)
le = LabelEncoder()
df['Transmission_encoded'] = le.fit_transform(df['Transmission'])
df = pd.get_dummies(df, columns=['Color'], drop_first=True)
print(df)


import pandas as pd
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler, MinMaxScaler
data = {
    'Age': [25, 30, 35, 40, 45],
    'Salary': [30000, 50000, 70000, 90000, 120000]
}
df = pd.DataFrame(data)
scaler_standard = StandardScaler()
df['Salary_standardized'] = scaler_standard.fit_transform(df[['Salary']])
scaler_minmax = MinMaxScaler()
df['Salary_normalized'] = scaler_minmax.fit_transform(df[['Salary']])
plt.figure(figsize=(12, 4))
plt.subplot(1, 3, 1)
plt.hist(df['Salary'], bins=10, color='skyblue', edgecolor='black')
plt.title("Original Salary")
plt.xlabel("Salary")
plt.ylabel("Frequency")
plt.subplot(1, 3, 2)
plt.hist(df['Salary_standardized'], bins=10, color='lightgreen', edgecolor='black')
plt.title("Standardized Salary")
plt.xlabel("Scaled Value")
plt.ylabel("Frequency")
plt.subplot(1, 3, 3)
plt.hist(df['Salary_normalized'], bins=10, color='salmon', edgecolor='black')
plt.title("Normalized Salary")
plt.xlabel("Scaled Value")
plt.ylabel("Frequency")
plt.tight_layout()
plt.show()


import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures
from sklearn.metrics import r2_score
import matplotlib.pyplot as plt
X = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9]).reshape(-1, 1)
y = np.array([1, 4, 9, 16, 25, 36, 49, 64, 81])  
lin_reg = LinearRegression()
lin_reg.fit(X, y)
y_pred_linear = lin_reg.predict(X)
r2_linear = r2_score(y, y_pred_linear)
poly = PolynomialFeatures(degree=2)
X_poly = poly.fit_transform(X)
lin_reg_poly = LinearRegression()
lin_reg_poly.fit(X_poly, y)
y_pred_poly = lin_reg_poly.predict(X_poly)
r2_poly = r2_score(y, y_pred_poly)
print(f"R^2 score with original features: {r2_linear:.4f}")
print(f"R^2 score with polynomial features: {r2_poly:.4f}")
plt.scatter(X, y, color='blue', label='Actual Data')
plt.plot(X, y_pred_linear, color='red', label='Linear Fit')
plt.plot(X, y_pred_poly, color='green', 
         label='Polynomial Fit (degree=2)')
plt.title("Linear vs Polynomial Regression")
plt.xlabel("X")
plt.ylabel("y")
plt.legend()
plt.show()