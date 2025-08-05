
from flask import Flask, render_template, request, redirect, url_for
import pickle
import numpy as np
import pandas as pd

app = Flask(__name__)
app.secret_key = "change-this-secret"

model = pickle.load(open("model.pkl", "rb"))
scaler = pickle.load(open("scaler.pkl", "rb"))
movies_meta = pd.read_csv("movies_meta.csv")

genre_cols = [c for c in movies_meta.columns if c not in ['movieId', 'title']]
movies_meta.set_index('movieId', inplace=True)

def movie_features(movie_id, user_avg):
    if movie_id not in movies_meta.index:
        # fallback zero vector
        genres = np.zeros(len(genre_cols))
    else:
        row = movies_meta.loc[movie_id]
        genres = row[genre_cols].values.astype(float)
    # append user_avg as last feature
    feat = np.concatenate([genres, np.array([user_avg])])
    return feat.reshape(1, -1)

@app.route("/", methods=["GET", "POST"])
def index():
    prediction = None
    proba = None
    recs = None
    # prepare movie options for dropdown (id | title)
    movies_list = [(int(mid), movies_meta.loc[int(mid)]['title']) for mid in movies_meta.index]
    movies_list = sorted(movies_list, key=lambda x: x[1].lower())
    if request.method == "POST":
        try:
            movie_id = int(request.form.get("movie"))
            # The app allows either pick existing user id to autofill avg, or provide avg manually
            user_avg_input = request.form.get("user_avg").strip()
            if user_avg_input == "":
                # optional: if they provide a user id, try to compute average from dataset stored in movies_meta? Not available
                user_avg = float(3.0)  # default neutral average
            else:
                user_avg = float(user_avg_input)

            # Build feature, scale and predict
            feat = movie_features(movie_id, user_avg)
            feat_scaled = scaler.transform(feat)
            pred = model.predict(feat_scaled)[0]
            probs = model.predict_proba(feat_scaled)[0]
            prediction = "Will Like ✅" if pred == 1 else "May Not Like ❌"
            proba = float(np.max(probs))

            all_feats = []
            all_ids = []
            for mid in movies_meta.index:
                all_ids.append(int(mid))
                all_feats.append(movie_features(int(mid), user_avg).ravel())
            all_feats = np.vstack(all_feats)
            all_feats_scaled = scaler.transform(all_feats)
            probas = model.predict_proba(all_feats_scaled)[:, 1]  # probability of liked
            top_idx = np.argsort(probas)[::-1][:10]  # top 10
            recs = [(all_ids[i], movies_meta.loc[all_ids[i]]['title'], float(probas[i])) for i in top_idx]

        except Exception as e:
            prediction = f"Error: {e}"

    return render_template("index.html",
                           movies=movies_list,
                           prediction=prediction,
                           proba=proba,
                           recs=recs)

if __name__ == "__main__":
   
    app.run(debug=True)
