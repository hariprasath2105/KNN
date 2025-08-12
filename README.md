# Movie Recommendation App (KNN + Flask)

This is a simple web application that predicts whether a user will **like** a selected movie based on their average rating and the movie's genre, using the **K-Nearest Neighbors (KNN)** algorithm.  
It also suggests **top recommended movies** for the given user profile.

---

## Dataset

We use the **MovieLens 100k** dataset from GroupLens:
- **Ratings** file (`u.data`): userId, movieId, rating, timestamp  
- **Movies** file (`u.item`): movieId, title, genres (19 binary flags)

---

## Features Used
For each `(user, movie)` pair:
- **Movie genres** → 19 binary columns
- **User average rating** → mean rating given by that user

**Label**:  
- `1` → Liked (rating >= 4)  
- `0` → Not liked (rating < 4)

---

## Tech Stack

- **Python 3**
- **Flask** (web framework)
- **scikit-learn** (machine learning, KNN)
- **pandas**, **numpy** (data processing)
- **HTML/CSS** (frontend UI)

![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Flask](https://img.shields.io/badge/Flask-000000?style=for-the-badge&logo=flask&logoColor=white)
![HTML](https://img.shields.io/badge/HTML5-E34F26?style=for-the-badge&logo=html5&logoColor=white)
![CSS](https://img.shields.io/badge/CSS3-1572B6?style=for-the-badge&logo=css3&logoColor=white)
![scikit-learn](https://img.shields.io/badge/scikit--learn-F7931E?style=for-the-badge&logo=scikit-learn&logoColor=white)
![Pandas](https://img.shields.io/badge/Pandas-150458?style=for-the-badge&logo=pandas&logoColor=white)

---

## Project Structure

```
KNN/
│
├── static/
│   └── style.css        
│
├── templates/
│   └── index.html       
│
├── app.py              
├── model.py              
├── model.pkl             
├── scaler.pkl              
├── movies_meta.csv     
├── u.data            
├── u.item               
└── README.md               
```

---

## How to Run

### 1. Install dependencies
```bash
pip install flask scikit-learn pandas numpy
```

### 2. Train the model
```bash
python model.py
```

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

<img width="916" height="554" alt="image" src="https://github.com/user-attachments/assets/4951054b-f96b-4424-a480-d76f5b1878d7" />

<img width="916" height="644" alt="image" src="https://github.com/user-attachments/assets/c9d8aa26-88af-4afd-b96b-2cf7c1880ae2" />

---
