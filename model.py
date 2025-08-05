import os
import pandas as pd
import numpy as np
import pickle
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import classification_report, accuracy_score

ML100K_DIR = "."   
U_DATA = os.path.join(ML100K_DIR, "u.data")
U_ITEM = os.path.join(ML100K_DIR, "u.item")

ratings_cols = ["userId", "movieId", "rating", "timestamp"]
ratings = pd.read_csv(U_DATA, sep="\t", names=ratings_cols, encoding='latin-1')

item_cols = [
 "movieId", "title", "release_date", "video_release_date", "IMDb_URL",
 "unknown", "Action", "Adventure", "Animation", "Children's", "Comedy",
 "Crime", "Documentary", "Drama", "Fantasy", "Film-Noir", "Horror", "Musical",
 "Mystery", "Romance", "Sci-Fi", "Thriller", "War", "Western"
]
movies = pd.read_csv(U_ITEM, sep="|", names=item_cols, encoding='latin-1')

genre_cols = item_cols[5:]
movies_meta = movies[["movieId", "title"] + genre_cols].copy()
movies_meta['movieId'] = movies_meta['movieId'].astype(int)

user_avg = ratings.groupby('userId')['rating'].mean().rename('user_avg').reset_index()

df = ratings.merge(movies_meta, on='movieId', how='left')
df = df.merge(user_avg, on='userId', how='left')

df['liked'] = (df['rating'] >= 4).astype(int)

features = genre_cols + ['user_avg']
X = df[features].fillna(0).values
y = df['liked'].values

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42, stratify=y
)

scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

knn = KNeighborsClassifier(n_neighbors=9, weights='distance')
knn.fit(X_train_scaled, y_train)

y_pred = knn.predict(X_test_scaled)
print("Accuracy:", accuracy_score(y_test, y_pred))
print(classification_report(y_test, y_pred))

with open("model.pkl", "wb") as f:
    pickle.dump(knn, f)

with open("scaler.pkl", "wb") as f:
    pickle.dump(scaler, f)

movies_meta.to_csv("movies_meta.csv", index=False)

