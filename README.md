# 📰 Persian News Publisher with AI Classification

A local web application for publishing Persian news with **automatic AI-powered categorization**.  
This project also serves as a **dataset collection tool** for training Persian NLP classification models.

---

## 🎯 Project Purpose

- Publish and store Persian news articles
- Automatically classify news using an LLM
- Build a labeled dataset for training Persian text classification models
- Export CSV and JSON datasets ready for ML pipelines

---

## 🗂️ Project Structure

```
news_app/
├── server.py             # Flask backend + AI API integration
├── news_publisher.html   # Full frontend (HTML/CSS/JS)
└── README.md
```

---

## ⚙️ Requirements

- Python 3.8+
- pip

---

## 🚀 Setup & Installation

### 1. Clone the repository

```bash
git clone https://github.com/your-username/news-publisher.git
cd news-publisher
```

### 2. Install dependencies

```bash
pip install flask flask-cors openai
```

### 3. Get a free API Key

Go to **[openrouter.ai](https://openrouter.ai)**, sign up, and create a free API Key.

### 4. Set your API Key in server.py

Open `server.py` and replace the placeholder:

```python
api_key="YOUR_API_KEY_HERE"
```

### 5. Run the server

```bash
python server.py
```

### 6. Open the app

Navigate to:

```
http://127.0.0.1:5000
```

---

## 📁 Project Files

### server.py

Flask backend that:
- Serves the HTML frontend
- Receives classification requests from the frontend
- Sends news text to the AI API
- Returns the suggested category

### news_publisher.html

Full frontend including:
- News submission form with automatic AI classification
- News table with category filter
- Statistics dashboard (total news, active categories)
- CSV and JSON export for ML use
- Local storage persistence

---

## 🏷️ Supported Categories

| Category | Description |
|----------|-------------|
| سیاسی (Political) | Domestic and international politics |
| ورزشی (Sports) | Sports news |
| اقتصادی (Economic) | Economy and market news |
| نظامی (Military) | Military and defense news |
| امنیتی (Security) | Security and law enforcement news |
| اجتماعی (Social) | Social and cultural news |
| فناوری (Technology) | Tech and innovation news |

---

## 📊 Dataset Output

After publishing news, export the dataset in two formats:

**CSV:**
```
متن خبر, دسته‌بندی, اهمیت, تاریخ, تشخیص_AI
"تیم ملی فوتبال ایران...", ورزشی, مهم, ۱۴۰۳/۳/۲۰, Yes
```

**JSON:**
```json
[
  {
    "id": 1234567890,
    "text": "تیم ملی فوتبال ایران...",
    "cat": "ورزشی",
    "priority": "مهم",
    "date": "۱۴۰۳/۳/۲۰",
    "aiTagged": true
  }
]
```

---

## 🔄 Using the Dataset in ML

```python
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.pipeline import Pipeline

# Load dataset
df = pd.read_csv('news_dataset.csv')

# Train model
pipeline = Pipeline([
    ('tfidf', TfidfVectorizer()),
    ('clf', MultinomialNB())
])

pipeline.fit(df['متن خبر'], df['دسته‌بندی'])
```

---

## 🛠️ Tech Stack

- **Backend:** Python, Flask, Flask-CORS
- **Frontend:** HTML, CSS, Vanilla JavaScript
- **AI:** OpenRouter API (free models)
- **Storage:** Browser localStorage

---

## 📌 Important Notes

- Do not close the CMD window — the server must stay running
- Never upload your API Key to GitHub
- For production use, replace Flask dev server with Gunicorn or uWSGI

---

## 🔐 Security

Create a `.gitignore` file to prevent leaking your API Key:

```
.env
__pycache__/
```

Store your API Key in a `.env` file:

```env
API_KEY=your_api_key_here
```

And load it in `server.py`:

```python
import os
from dotenv import load_dotenv
load_dotenv()
api_key = os.getenv("API_KEY")
```

---

## 📄 License

MIT License
