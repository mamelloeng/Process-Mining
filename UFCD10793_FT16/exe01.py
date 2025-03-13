import pandas as pd

casts = pd.read_csv('cast.csv', index_col=None)

print(casts.describe())

print(casts.head())

titles = pd.read_csv('titles.csv', index_col =None)

print(titles.tail())

pd.set_option('display.max_rows', 10, 'display.max_columns', 10)

print(titles)

tamanho=len(titles)

print(tamanho)

print(titles.head(3))

t = titles['title']

print(type(t))
