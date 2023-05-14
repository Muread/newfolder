import pandas as pd
recipes = pd.read_csv('recipes_sample.csv', index_col=0)
reviews = pd.read_csv('reviews_sample.csv', index_col=0, parse_dates=['date'])
total = 0
count = 0
for index, row in reviews.iterrows():
    if row['date'].year == 2010:
        total += row['rating']
        count += 1

mean_rating = total / count
mean_rating = reviews.loc[reviews['date'].dt.year == 2010, 'rating'].mean()
