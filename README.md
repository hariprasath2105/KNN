
# 🎬 Movie Recommendation App (KNN + Flask)

This is a simple web application that predicts whether a user will **like** a selected movie based on their average rating and the movie's genre, using the **K-Nearest Neighbors (KNN)** algorithm.  
It also suggests **top recommended movies** for the given user profile.

---

## 📊 Dataset

We use the **MovieLens 100k** dataset from GroupLens:
- **Ratings** file (`u.data`): userId, movieId, rating, timestamp  
- **Movies** file (`u.item`): movieId, title, genres (19 binary flags)

You can download the dataset here:  
[MovieLens 100k Download](http://files.grouplens.org/datasets/movielens/ml-100k.zip)

After downloading, extract and place the following files into your project folder:
- `u.data`
- `u.item`

---

## 🧠 Features Used
For each `(user, movie)` pair:
- **Movie genres** → 19 binary columns
- **User average rating** → mean rating given by that user

**Label**:  
- `1` → Liked (rating >= 4)  
- `0` → Not liked (rating < 4)

---

## 🛠 Tech Stack

- **Python 3**
- **Flask** (web framework)
- **scikit-learn** (machine learning, KNN)
- **pandas**, **numpy** (data processing)
- **HTML/CSS** (frontend UI)

---

## 📁 Project Structure

```
KNN/
│
├── static/
│   └── style.css           # Gradient UI styling
│
├── templates/
│   └── index.html          # Web form & results
│
├── app.py                  # Flask backend
├── model.py                # Train KNN & save model
├── model.pkl               # Trained KNN model
├── scaler.pkl              # Scaler for features
├── movies_meta.csv         # Movies & genre data
├── u.data                  # Ratings file (from MovieLens)
├── u.item                  # Movies metadata file (from MovieLens)
└── README.md               # This file
```

---

## 🚀 How to Run

### 1. Install dependencies
```bash
pip install flask scikit-learn pandas numpy
```

### 2. Train the model
```bash
python model.py
```
This will generate:
- `model.pkl`
- `scaler.pkl`
- `movies_meta.csv`

### 3. Run the app
```bash
python app.py
```

### 4. Open in browser
Go to:  
[http://127.0.0.1:5000](http://127.0.0.1:5000)

---

## 🖥 Example Usage

1. Select a movie from the dropdown.  
2. Enter your average rating (1.0 - 5.0).  
3. Click **Predict & Recommend**.  
4. The app will:
   - Predict if you'll like the movie
   - Show top 10 recommended movies with confidence scores

---

## 📌 Notes
- If `user_avg` is left blank, the app uses a default value of **3.0**.
- The recommendations are based only on movie genres and your average rating — no collaborative filtering is applied.
- For a better model, more user-specific data and ratings should be included.

---

## 🙋 Author
**Hari Prasath S**  
GitHub: [@hariprasath2105](https://github.com/hariprasath2105)
