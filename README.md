# Customer Feedback — Streamlit (Standalone)

A simple, version-safe Streamlit app for collecting customer ratings and comments.

## Features
- Star rating (1–5), comments
- Optional name, email, phone
- Persists to **feedback_data.csv** in the app folder
- Basic **Admin Dashboard** (unlock with any non-empty PIN in the sidebar)
- Export all feedback to CSV

## Run locally
```bash
pip install -r requirements.txt
streamlit run app.py
```
