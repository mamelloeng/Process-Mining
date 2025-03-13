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

tamanhocasts=len(casts)
print(tamanhocasts)

casts.info()

print(titles.iloc[0])

after85 = titles[titles['year'] > 1985]
print(after85.head())

t = titles

movies90 = t[(t['year']>=1990) & (t['year']<2000)]
print(movies90.head())

macbeth = t[t['title'] == 'Macbeth'].sort_index()
print(macbeth.head())

macbeth = t[t['title'] == 'Macbeth'].sort_values('year')
print(macbeth.head())

print(casts.loc[3:4],'\n')

c = casts

print(c['n'].isnull().head())

print(c[c['n'].isnull()].head(3),'\n')

c_fill = c[c['n'].isnull()].fillna('NA')
print(c_fill.head(2))

t = titles

print(t[t['title'] == 'Maa'],'\n')

print(t[t['title'].str.startswith("Maa ")].head(3),'\n')

print(t['year'].value_counts().head())

c = casts

cf = c[c['name'] == 'Aaron Abrams']

print(cf.groupby(['year']).size().head())
print(t.groupby(['year']).size().head())

gbmultiplecolumns = cf.groupby(['year','title']).size()
print(gbmultiplecolumns.head())

