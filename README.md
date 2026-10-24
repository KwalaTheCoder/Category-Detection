# Persian News Category Detection

A compact Flask application for publishing Persian news, suggesting categories with Gemini, and exporting labeled data for NLP experiments.

## Features

- Persian, right-to-left publishing interface
- AI-assisted news categorization
- Browser-based local storage
- CSV and JSON dataset export
- Simple Flask API and vanilla HTML/CSS/JavaScript frontend

## Run locally

```bash
python -m venv .venv
pip install flask flask-cors google-generativeai
```

Set credentials outside the source code:

```bash
# PowerShell
$env:GEMINI_API_KEY="your-key"
$env:GEMINI_MODEL="gemini-1.5-flash"

# macOS/Linux
export GEMINI_API_KEY="your-key"
export GEMINI_MODEL="gemini-1.5-flash"
```

Then start the app:

```bash
python server.py
```

Open `http://127.0.0.1:5000`.

## Structure

- `server.py` — Flask backend and Gemini integration
- `news_publisher.html` — complete browser interface

## Notes

AI labels should be reviewed before being used as training data. Never commit API keys or exported private datasets.
