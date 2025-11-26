#!/usr/bin/env python
# coding: utf-8

# # Линейная регрессия

# In[3]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.datasets import make_regression
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import scale, PolynomialFeatures
from sklearn.linear_model import LinearRegression, Ridge, Lasso, ElasticNet
from sklearn.metrics import mean_absolute_percentage_error, mean_squared_error, r2_score


# In[4]:


# Линейная регрессия на основе матричного метода
class MatrixLinearRegression:

    def fit(self, X, y):
        X = np.insert(X, 0, 1, axis=1)   # add ones vector
        XT_X_inv = np.linalg.inv(X.T @ X)   # (X.T * X) ** (-1) inverse matrix
        weights = np.linalg.multi_dot([XT_X_inv, X.T, y])   # XT_X_inv * X.T * y
        self.bias, self.weights = weights[0], weights[1:]

    def predict(self, X_test):
        return X_test @ self.weights + self.bias


# In[48]:


# Линейная регрессия на основе пакетного градиентного спуска
class GDLinearRegression:
    def __init__(self, learning_rate=0.01, tolerance=1e-8):
        self.learning_rate = learning_rate
        self.tolerance = tolerance

    def fit(self, X, y):
        n_samples, n_features = X.shape
        self.bias, self.weights = 0, np.zeros(n_features)
        previous_db, previous_dw = 0, np.zeros(n_features)

        while True:
            y_pred = X @ self.weights + self.bias
            db = 1 / n_samples * np.sum(y_pred - y)
            dw = 1 / n_samples * X.T @ (y_pred - y)
            self.bias -= self.learning_rate * db
            self.weights -= self.learning_rate * dw

            abs_db_reduction = np.abs(db - previous_db)
            abs_dw_reduction = np.abs(dw - previous_dw)

            if abs_db_reduction < self.tolerance:
                if abs_dw_reduction.all() < self.tolerance:
                    break

            previous_db = db
            previous_dw = dw

    def predict(self, X_test):
        return X_test @ self.weights + self.bias


# In[51]:


# Загружаем датасет
file = 'author_ru_utf.csv'
df = pd.read_csv(file, sep = ',', header = 0)
df = df.loc[:, 'document':'Author']
df.head()


# In[52]:


# матрица корреляций
correlation_matrix = df.loc[:, 'на':'из-за'].corr()
correlation_matrix.style.background_gradient(cmap='coolwarm')


# In[55]:


# Создаем выборку с признаками-переменными (предлогами) и выборку с признаками для предсказания
x1, y1 = df.loc[:, ['а','но']], df.loc[:, 'и'] # зависимость "но" от "что" и "и"
x1_scaled = scale(x1)
x1_train, x1_test, y1_train, y1_test = train_test_split(x1, y1, random_state=0)
x1_train_s, x1_test_s, y1_train, y1_test = train_test_split(x1_scaled, y1, random_state=0)
print(df)


# In[ ]:


# Линейная регрессия матричным методом
matrix_linear_regression = MatrixLinearRegression()
matrix_linear_regression.fit(x1_train, y1_train) # применение класса матричной регрессии
matrix_lr_pred_res = matrix_linear_regression.predict(x1_test) # предсказание на тестовых данных
matrix_lr_r2 = r2_score(y1_test, matrix_lr_pred_res) # вычисление R2-score (1-SSres/SStot)
matrix_lr_mape = mean_absolute_percentage_error(y1_test, matrix_lr_pred_res)

print(f'Matrix Linear regression  R2 score: {matrix_lr_r2}')
print(f'Matrix Linear regression MAPE: {matrix_lr_mape}', '\n')

print(f'weights: {matrix_linear_regression.bias, *matrix_linear_regression.weights}')
print(f'prediction: {matrix_lr_pred_res}')


# In[47]:


# градиентный спуск
linear_regression = GDLinearRegression()
linear_regression.fit(x1_train, y1_train)
pred_res = linear_regression.predict(x1_test)
r2 = r2_score(y1_test, pred_res)
mape = mean_absolute_percentage_error(y1_test, pred_res)

print(f'Linear regression R2 score: {r2}')
print(f'Linear regression MAPE: {mape}', '\n')

print(f'weights: {linear_regression.bias, *linear_regression.weights}')
print(f'prediction: {pred_res}')


# In[ ]:




