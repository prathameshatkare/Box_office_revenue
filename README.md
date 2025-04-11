

---

```markdown
# 🎬 Box Office Revenue Predictor

A machine learning-powered Streamlit web app that predicts the **domestic box office revenue** of a movie based on various factors such as distributor, release details, genres, and more.

### 🚀 Live Demo
👉 [Check it out here](https://boxofficerevenueprathameshatkare.streamlit.app/)  


---

## 📦 Features

- Predicts domestic revenue using a trained **XGBoost Regressor**
- Clean UI built with **Streamlit**
- Handles genre encoding and label transformations
- Shows prediction history (CSV logged)
- Simple deployment using **Streamlit Cloud**

---

## 🧠 Tech Stack

- Python
- Pandas & NumPy
- Scikit-learn & XGBoost
- Streamlit
- Joblib (for model serialization)

---

## 🛠️ Installation

1. **Clone the repository**  
```bash
git clone https://github.com/prathameshatkare/Box_office_revenue.git
cd box-office-streamlit
```

2. **Install dependencies**  
```bash
pip install -r requirements.txt
```

3. **Run the app locally**  
```bash
streamlit run app.py
```

---

## 📁 Project Structure

```
├── app.py                   # Streamlit UI script
├── box_office_pipeline_model.pkl  # Trained ML model
├── prediction_history.csv   # (Auto-created) Logs past predictions
├── requirements.txt         # Python dependencies
└── README.md
```

---

## 🧪 Example Input

| Feature            | Example           |
|--------------------|-------------------|
| Distributor        | Warner Bros.      |
| MPAA Rating        | PG-13             |
| Opening Theaters   | 3500              |
| Release Days       | 45                |
| Genre              | Action            |

---

## 📊 Model Info

- Trained using `XGBoostRegressor`
- Features include: Distributor, MPAA, Theaters, Release Time, Genres
- Target: `Domestic Revenue` (log-transformed for regression)

---

## 📜 License

MIT License. Feel free to use, remix, and share!

---

## 💬 Feedback

If you find a bug or want to suggest a feature, feel free to [open an issue](https://github.com/prathameshatkare/Box_office_revenue).

```

---

