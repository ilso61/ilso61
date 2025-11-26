#!/usr/bin/env python
# coding: utf-8

# # Наивный Баесовский классификатор

# In[63]:


import pandas as pd
from sklearn.naive_bayes import MultinomialNB
from sklearn.model_selection import train_test_split
from matplotlib import pyplot as plt
from scipy.stats import norm
import numpy as np


# In[44]:


file = 'author_ru_utf.csv'
df = pd.read_csv(file, sep = ',', header = 0)
df = df.loc[:, 'document':'Author']
df.head()


# In[61]:


# Приготовить данные
X = df.loc[:, 'на' : 'из-под']
Y = df['Author']
Y.head()


# In[66]:


X_train, X_test, y_train, y_test = train_test_split(X, Y, test_size=0.2, random_state=42)

model = MultinomialNB()

model.fit(X_train, y_train)


# In[67]:


y_pred = model.predict(X_test)


# In[68]:


from sklearn.metrics import accuracy_score, classification_report
from sklearn.metrics import confusion_matrix, ConfusionMatrixDisplay
# Подсчитать 
accuracy = accuracy_score(y_test, y_pred)
print(f"Accuracy: {accuracy}")
print(classification_report(y_test, y_pred))


# In[72]:


cm = confusion_matrix(y_test, y_pred)

# 6. Plot the confusion matrix using ConfusionMatrixDisplay
# You can customize labels and other plot parameters
disp = ConfusionMatrixDisplay(confusion_matrix=cm, display_labels=['Гоголь', 'Гончаров', 'Достоевский', 'Толстой'])
disp.plot(cmap=plt.cm.Blues) # Choose a colormap
plt.title('Confusion Matrix')
plt.show()


# In[ ]:





# In[ ]:




