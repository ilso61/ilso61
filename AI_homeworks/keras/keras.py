#!/usr/bin/env python
# coding: utf-8

# In[62]:


import matplotlib.pyplot as plt
import pandas as pd
df = pd.read_csv('author_ru_utf.csv', sep = ',', encoding = 'utf8')
df.head()


# In[63]:


# Заменяем авторов на числа
print(list(set(df['Author'])))
authors_dict = {}
for i in range(len(list(set(df['Author'])))):
    authors_dict.update({list(set(df['Author']))[i]: i})
print(authors_dict)
df['Author'] = df['Author'].replace(authors_dict)
df.head()


# In[64]:


# матрица корреляций
correlation_matrix = df.loc[:, 'на':'Author'].corr()
correlation_matrix.style.background_gradient(cmap='coolwarm')


# In[65]:


# Перемешаем значения, чтобы случайно выбирать тестовую выборку
df = df.sample(frac=1).reset_index(drop=True)
df.head()


# In[95]:


# Я объединил предлоги и союзы в группы по интегральной семе, ну +- СПОЙЛЕР не помогло улучшить
possession = ["с", "со", "без"] 
loc_in_space = ["при"]
dir_from = ["из-за", "из-под"] #["от", "из", "из-за", "из-под"]
dir_to = ["к", "ко", "до"]
move_by_obj = ["через", "по"] #
dir_loc = ["на", "в", "во", "под", "над", "за"] #
about = ["про"]
for_ = ["для"]
that = ["что"]
coord = ["и", "но", "а"]
# Теперь посчитаем суммы этих групп слов и сделаем их отдельными датафреймами, а не сериес обджектам, на всякий случай
Possession = pd.DataFrame(df.loc[:, possession].sum(axis=1))
Near = pd.DataFrame(df.loc[:, loc_in_space])
Dir_from = pd.DataFrame(df.loc[:, dir_from].sum(axis=1))
Move_by_obj = pd.DataFrame(df.loc[:, move_by_obj].sum(axis=1))
Dir_loc = pd.DataFrame(df.loc[:, dir_loc].sum(axis=1))
About = pd.DataFrame(df.loc[:, about].sum(axis=1))
For_ = pd.DataFrame(df.loc[:, for_])
That = pd.DataFrame(df.loc[:, that])
Coord = pd.DataFrame(df.loc[:, coord].sum(axis=1))
df_new = pd.concat([Possession,Near,Dir_from,Move_by_obj,Dir_loc,About,For_,That,Coord], axis = 1)
#df_new = pd.concat([Dir_from, Move_by_obj, About, Coord], axis = 1) Вот с этими параметрами получается также, как и с другими
df_new


# In[96]:


from keras.models import Sequential
from keras.layers import Dense, Activation

import numpy as np

def get_model():
    # function returns the many-layered feedforward network
    # considers 9 floating point numbers as input
    # produces 2 floating point numbers as output
    model = Sequential()
    model.add(Dense(18, activation='relu', input_dim=9))
    # uncomment the following line to add one more layer
    # model.add(Dense(9, activation='relu'))
    model.add(Dense(2, activation='softmax'))
    model.compile(optimizer='adam',
                  loss='mean_squared_error',
                  metrics=['accuracy'])
    return model

def prepare_data(param_df, df_with_label): # переделал, чтобы лейблы загружались с исходного df, а параметры с df_new
    # function reads data from @filename
    # and returns six arrays: train data, train labels,
    # validation data, validation labels, test data and test labels
    input_data = np.ndarray(shape=(456, 9), dtype=float)
    output_data = np.ndarray(shape=(456, 1), dtype=float)
    input_data[:, :] = param_df.loc[:, :].to_numpy(dtype = float)
    output_data[:, :] = pd.DataFrame(df_with_label.loc[:, 'Author']).to_numpy(dtype = float)

    train_data = np.ndarray(shape=(273, 9), dtype=float)
    train_labels = np.ndarray(shape=(273, 1), dtype=float)
    train_data[:, :] = input_data[:273, :]
    train_labels[:, :] = output_data[:273, :]

    valid_data = np.ndarray(shape=(91, 9), dtype=float)
    valid_labels = np.ndarray(shape=(91, 1), dtype=float)
    valid_data[:, :] = input_data[273:364, :]
    valid_labels[:, :] = output_data[273:364, :]

    test_data = np.ndarray(shape=(92, 9), dtype=float)
    test_labels = np.ndarray(shape=(92, 1), dtype=float)
    test_data[:, :] = input_data[364:, :]
    test_labels[:, :] = output_data[364:, :]

    return train_data, train_labels, valid_data, valid_labels, test_data, test_labels


# In[97]:


# getting data for both training and testing
train_data, train_labels, valid_data, valid_labels, test_data, test_labels = prepare_data(df_new, df)

print(train_data.shape)
print(train_labels.shape)
print(valid_data.shape)
print(valid_labels.shape)
print(test_data.shape)
print(test_labels.shape)


# In[98]:


# creating a model
model = get_model()

# training a model
model.fit(train_data, train_labels, validation_data=(valid_data, valid_labels),
          epochs=100, batch_size=32)

# computing network predictions
predictions = model.predict_on_batch(test_data)




# In[99]:


# computing the percentage of correct predictions
res = 0.0
for i in range(test_data.shape[0]):
    if (test_labels[i, 0] == predictions[i, 0]):
        res += 1.0
res /= float(test_data.shape[0])

# printing resulting percentage
print('-------------------')
print(res * 100.0)
print('-------------------')

