import pandas as pd
import matplotlib.pyplot as plt

pd.set_option('display.max_columns', None)
movies = pd.read_csv(r'C:\Users\hp\Downloads\ml-latest-small\ml-latest-small\movies.csv')
ratings = pd.read_csv(r'C:\Users\hp\Downloads\ml-latest-small\ml-latest-small\ratings.csv')

print(movies.head())
print(ratings.head())

print(movies.isnull().sum())
print(ratings.isnull().sum())


print(movies.info())

print("\n")
movies_data = pd.merge(movies, ratings, on='movieId')
# Display the first few rows of the merged data

print(movies_data.head())
print("\n 10 Top-Rated Movies:")
avg_ratings = movies_data.groupby('title')['rating'].mean().sort_values(ascending=False)
print(avg_ratings.head(10))

bars,counts,bins = plt.hist(movies_data['rating'], bins= 10, edgecolor ='black')
for bar, count in zip(bars, counts):
    plt.text(bar.get_x() + bar.get_width() / 2, count, str(int(count)), ha='center', va='center', fontsize=10)

plt.title("Distribution of Ratings")
plt.xlabel("ratings")
plt.ylabel("frequency")
plt.show()

popular_movies=movies_data.groupby('title').filter(lambda x : len(x) >= 50)
top_movies = popular_movies.groupby('title')['rating'].mean().sort_values(ascending=False).head(10)

ax = top_movies.plot(kind='bar', title='Top 10 Movies with at Least 50 Ratings', figsize=(20, 10), color='skyblue', edgecolor='black')
plt.ylabel("average rating")
for i, value in enumerate(top_movies):
    plt.text(i, value, f'{value:.2f}', ha='center', va='bottom', fontsize=10)

plt.xticks(rotation=45, ha='right', fontsize=10)
plt.tight_layout()

plt.show()