# 📝 Customer Feedback System — Streamlit App

A lightweight and secure **customer feedback collection app** built using **Streamlit**.  
It allows users to submit their experience ratings and comments while giving administrators a dashboard to view, export, and analyze feedback.

---

## 🎯 Purpose
The app provides an easy way for businesses to collect, store, and manage customer feedback digitally — without needing a backend database.

---

## ⚙️ Features

### 💬 For Customers
- ⭐ Rate experience (1–5 stars)
- 🗒️ Add comments and suggestions
- 🧑 Optional fields: Name, Email, Phone
- ✅ Data stored locally for privacy

### 🔒 For Admins
- Access protected by **Admin PIN: `7911`**
- View all submitted feedback
- See total submissions and average rating
- Download all feedback as a CSV file

---

## 🛠️ Tech Stack
- **Python 3.9+**
- **Streamlit**
- **Pandas**
- Built-in local CSV storage (no external database required)

---

## 📂 Project Structure
```
customer_feedback_app/
│
├── app.py                 # Main Streamlit app
├── requirements.txt       # Dependencies
├── feedback_data.csv      # Auto-created storage for feedback (after first run)
└── README.md              # This file
```

---

## ▶️ Run the App Locally

1. Clone or download this repository:
   ```bash
   git clone https://github.com/<your-username>/customer-feedback-app.git
   cd customer-feedback-app
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Run the app:
   ```bash
   streamlit run app.py
   ```

4. Open your browser at [http://localhost:8501](http://localhost:8501)

---

## 🔑 Admin Access
To open the Admin Dashboard:
1. Go to the sidebar in the app.
2. Enter the Admin PIN → **`7911`**
3. Access the full dashboard:
   - View all feedback
   - Export as CSV
   - Check average ratings and totals

---

## 📊 Data Storage
All feedback is stored automatically in a file named:
```
feedback_data.csv
```
This file is saved in the same folder as the app and updates every time a new feedback form is submitted.

---

## 🌱 Future Enhancements
- Add Google Sheets or cloud database integration.
- Enable email notifications for new feedback.
- Add branch/store selection dropdown.
- Visualize feedback trends using Streamlit charts.

---

## 🧑‍💻 Author
**Umesh Chandra Karthikeya**  
🌐 [karthikeya.koduru07@icloud.com]

---

## 📜 License
This project is open-sourced under the **MIT License**.  
Feel free to use, modify, and distribute with proper attribution.

---
