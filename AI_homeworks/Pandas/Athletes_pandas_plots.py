#!/usr/bin/env python
# coding: utf-8

# # Задачи к Лекции 1
# 
# Дан файл "athlete_events", который содержит информацию об олимпийских чемпионах за последние 120 лет.

# **Чтение данных**
# 
# При загрузке оставляем только информацию о призерах с данными без пропусков.

# In[1]:


get_ipython().run_line_magic('matplotlib', 'inline')
import zipfile
import numpy as np
import pandas as pd
import seaborn as sns

z = zipfile.ZipFile("C:/Users/ilso61/Downloads/lolol/athlete_events.zip")
df = pd.read_csv(z.open("athlete_events.csv"))
df = df.dropna(subset=['Medal', "Age", "Height", "Weight"])
df.head()


# **Получение различной информации**

# In[2]:


df.shape


# In[3]:


df.info()


# In[4]:


df.describe()


# **1. Сколько мужчин и женщин получили золотые, серебрянные и бронзовые медали?**

# In[9]:


# Your code here
df['Medal'].value_counts()


# **2. Какая страна получила наибольшее количество золотых медалей за всю историю олимпийских игр?**

# In[12]:


# Your code here
gold_medals = (df[df['Medal'] == 'Gold'])
gold_by_country = gold_medals.groupby('NOC').size().reset_index(name='Gold_Medals')
gold_by_country.sort_values('Gold_Medals', ascending=False).iloc[0]


# **3. Выведите распределение пола участника олимпиады от вида спорта (crosstab)**

# In[13]:


# Your code here
pd.crosstab(df['Sport'], df['Sex'], margins=True, margins_name='Total')


# **4. Выведите средний возраст и его стандартное отклонения для женщин, учавствовавших в хоккее на льду**

# In[15]:


# Your code here
women_hockey = df[(df['Sex'] == 'F') & (df['Sport'] == 'Ice Hockey')]
mean_age = women_hockey['Age'].mean()
std_age = women_hockey['Age'].std()
print(mean_age)
print(std_age)


# **5. У какой страны больше всего было больше всего женщин, получивших бронзовую медаль?**

# In[17]:


# Your code here
gold_medals = (df[df['Medal'] == 'Gold'])
gold_medals_F = (df[df['Sex'] == 'F'])
gold_by_country = gold_medals_F.groupby('NOC').size().reset_index(name='Gold_Medals')
gold_by_country.sort_values('Gold_Medals', ascending=False).iloc[0]


# **6. Постройте гистограмму распределения количества медалей (бронза, серебро, золото) для первых трех стран, получивших наибольшее количество медалей**

# In[21]:


# Your code here
import matplotlib.pyplot as plt
top_countries = df['NOC'].value_counts().head(3).index.tolist()
medal_counts = [] #новый датафрейм с количеством медалей у каждой из трех стран
for country in top_countries:
    country_medals =df[df['NOC'] == country]['Medal'].value_counts()
    medal_counts.append({
        'Country': country,
        'Gold': country_medals.get('Gold', 0),
        'Silver': country_medals.get('Silver', 0),
        'Bronze': country_medals.get('Bronze', 0),
        'Total': country_medals.sum()
    })

medal_df = pd.DataFrame(medal_counts)

# Горизонтальная гистограмма
fig, ax = plt.subplots(figsize=(12, 8))


bottom = np.zeros(len(top_countries))
colors = ['gold', 'silver', '#cd7f32']
medal_types = ['Gold', 'Silver', 'Bronze']

for i, medal_type in enumerate(medal_types):
    values = medal_df[medal_type].values
    ax.barh(top_countries, values, left=bottom, 
            label=medal_type, color=colors[i], alpha=0.8)
    bottom += values

ax.set_xlabel('Количество медалей', fontsize=12)
ax.set_title('Распределение медалей для топ-3 стран (стековая гистограмма)', 
             fontsize=14, fontweight='bold')
ax.legend()
ax.grid(axis='x', alpha=0.3)

plt.tight_layout()
plt.show()


# **7. Нарисуйте распределение веса мужчин, получивших серебрянную медаль(density или distplot)**

# In[22]:


# Your code here
silver_men = df[(df['Sex'] == 'M') & 
                (df['Medal'] == 'Silver') & 
                (df['Weight'])]
plt.figure(figsize=(12, 8))

plt.subplot(2, 2, 1)
sns.distplot(silver_men['Weight'], kde=True, hist=True, color='silver')
plt.title('Distplot: Распределение веса мужчин с серебряными медалями')
plt.xlabel('Вес (кг)')
plt.ylabel('Плотность')
plt.show()


# **8. Постройте boxplot для возраста участника в зависимости от медали**

# In[26]:


# Your code here
medal_winners = df[(df['Medal'].notna()) & (df['Age'].notna())]
plt.figure(figsize=(12, 8))

# Основной boxplot
sns.boxplot(data=medal_winners, x='Medal', y='Age', 
            order=['Gold', 'Silver', 'Bronze'],
            palette=['gold', 'silver', '#cd7f32'])
plt.title('Распределение возраста участников по типам медалей', 
          fontsize=16, fontweight='bold', pad=20)
plt.xlabel('Тип медали', fontsize=12)
plt.ylabel('Возраст (лет)', fontsize=12)
plt.grid(True, alpha=0.3)


plt.show()


# **9. Постройте pairplot для веса, возраста и роста участников от USA.**

# In[27]:


# Your code here
usa_athletes = df[(df['NOC'] == 'USA') & 
                  (df['Weight'].notna()) & 
                  (df['Age'].notna()) & 
                  (df['Height'].notna())]
plt.figure(figsize=(12, 10))
sns.pairplot(usa_athletes[['Age', 'Height', 'Weight']], 
             diag_kind='hist', 
             plot_kws={'alpha': 0.6, 's': 20},
             height=3)
plt.suptitle('Pairplot: Взаимосвязь возраста, роста и веса участников из США', 
             y=1.02, fontsize=16, fontweight='bold')
plt.tight_layout()
plt.show()


# ### Часть 2. NLP: BoW

# In[28]:


df_au = pd.read_csv("C:/Users/ilso61/Downloads/lolol/author_ru_utf.csv")
df_au.head()


# In[29]:


df_au.shape


# In[30]:


df_au.info()


# In[31]:


df_au.describe()


# **1. Какая служебная часть речи чаще всего встречается Н.В. Гоголя?**

# In[37]:


# Your code here
gogol_df = df_au[(df_au['Author'] == 'ГогольНВ')]
service_pos_columns = ['на', 'что', 'за', 'и', 'в', 'из', 'со', 'а', 'во', 'для', 'с', 'но', 'к', 'по', 
                     'от', 'под', 'до', 'про', 'о', 'ко', 'над', 'без', 'при', 'об', 'через', 'из-за', 'из-под']
service_pos_sums = gogol_df[service_pos_columns].sum()
most_common_service_pos = service_pos_sums.idxmax()
most_common_count = service_pos_sums.max()
print(service_pos_sums.sort_values(ascending=False).head())


# **2. Постройте гистограмму распределения предлогов "на", "с", "в" у авторов**

# In[43]:


# Your code here
plt.style.use('seaborn-v0_8')
sns.set_palette("husl")


# Подготовка данных для построения графиков
prepositions_data = df_au.melt(id_vars=['Author', 'document'], 
                          value_vars=['на', 'с', 'в'],
                          var_name='Предлог', 
                          value_name='Количество')

# Настройка стиля
plt.figure(figsize=(14, 8))
sns.set_style("whitegrid")

# вычисляем средние значения для каждого автора
prep_na = df_au.groupby('Author')['на'].mean()
prep_s = df_au.groupby('Author')['с'].mean()
prep_v = df_au.groupby('Author')['в'].mean()

# DataFrame для гистограммы
prep_df = pd.DataFrame({
    'Автор': prep_na.index.tolist() * 3,
    'Предлог': ['на'] * len(prep_na) + ['с'] * len(prep_s) + ['в'] * len(prep_v),
    'Средняя_частота': pd.concat([prep_na, prep_s, prep_v])
})

# Построение гистограммы
sns.barplot(data=prep_df, x='Автор', y='Средняя_частота', hue='Предлог', 
           palette=['#FF6B6B', '#4ECDC4', '#45B7D1'])

plt.title('Распределение предлогов "на", "с", "в" у авторов', fontsize=16, fontweight='bold', pad=20)
plt.xlabel('Автор', fontsize=12)
plt.ylabel('Средняя частота употребления', fontsize=12)
plt.xticks(rotation=45)
plt.legend(title='Предлог', title_fontsize=12)
plt.grid(axis='y', alpha=0.3)

plt.tight_layout()
plt.show()


# **3. Постройте boxplot для предлога "из-за" для авторов**

# In[44]:


# Your code here
plt.figure(figsize=(12, 8))
sns.set_style("whitegrid")

# Построение boxplot для предлога "из-за"
sns.boxplot(data=df_au, x='Author', y='из-за', palette='Set2')

plt.title('Распределение предлога "из-за" у авторов', fontsize=16, fontweight='bold', pad=20)
plt.xlabel('Автор', fontsize=12)
plt.ylabel('Количество употреблений', fontsize=12)
plt.grid(axis='y', alpha=0.3)


means = df_au.groupby('Author')['из-за'].mean()
for i, author in enumerate(means.index):
    plt.scatter(i, means[author], color='red', zorder=3, s=80, label='Среднее' if i == 0 else "")

plt.legend()
plt.tight_layout()
plt.show()


# **4. Создайте распределение предлога "за" по двум любым авторам**

# In[47]:


# Your code here

# Фильтруем данные
authors_data = df_au[df_au['Author'].isin(['ГогольНВ', 'ТолстойЛН'])]

# Основной график
plt.figure(figsize=(12, 8))

# Комбинированный график: гистограмма + KDE
sns.histplot(data=authors_data, x='за', hue='Author', bins=20, alpha=0.6, kde=True)
plt.title(f'Распределение предлога "за" у Гоголя Н.В. и Толстого Л.Н.', fontsize=16, fontweight='bold')
plt.xlabel('Количество употреблений предлога "за"')
plt.ylabel('Частота')
plt.legend(title='Автор')
plt.grid(alpha=0.3)

plt.tight_layout()
plt.show()


# In[ ]:




