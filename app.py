# app.py
# ------------------------------------------------------------
# Customer Feedback (Standalone) — Streamlit
# - Simple star rating + comments
# - Optional name/email/phone
# - Persists feedback to local CSV (feedback_data.csv)
# - Admin dashboard protected by a PIN (set via sidebar)
# - Version-safe: no experimental Streamlit APIs
# ------------------------------------------------------------

import os
import time
import pandas as pd
import streamlit as st
from datetime import datetime

st.set_page_config(page_title="Customer Feedback", page_icon="📝", layout="wide")

DATA_FILE = "feedback_data.csv"

# ---------------- Utilities ----------------
def load_data():
    if os.path.exists(DATA_FILE):
        try:
            return pd.read_csv(DATA_FILE)
        except Exception:
            return pd.DataFrame(columns=["timestamp","rating","category","comments","name","email","phone"])
    return pd.DataFrame(columns=["timestamp","rating","category","comments","name","email","phone"])

def append_row(row: dict):
    df = load_data()
    df = pd.concat([df, pd.DataFrame([row])], ignore_index=True)
    df.to_csv(DATA_FILE, index=False)

def avg_rating(df: pd.DataFrame):
    if df.empty or "rating" not in df:
        return 0.0
    try:
        return float(df["rating"].astype(float).mean())
    except Exception:
        return 0.0

def star_display(value: float) -> str:
    # Show rounded rating with stars
    filled = "★" * int(round(value))
    empty = "☆" * (5 - int(round(value)))
    return f"{filled}{empty} ({value:.2f}/5)"

# ---------------- Sidebar ----------------
st.sidebar.title("Feedback App")
st.sidebar.caption("A simple collector for customer reviews.")

# Optional: choose a category to display on the main form (your services/products)
categories_default = ["General Experience", "Product Quality", "Delivery", "Support", "Pricing"]
st.sidebar.write("Suggested categories (you can edit on the main form):")
st.sidebar.code(", ".join(categories_default))

st.sidebar.markdown("---")
admin_pin = st.sidebar.text_input("Admin PIN (to view dashboard)", type="password", help="Set a simple PIN like 1234")
st.sidebar.caption("Leave blank if you don't need the dashboard.")

# ---------------- Tabs ----------------
tab_feedback, tab_thanks, tab_admin = st.tabs(["Submit Feedback", "Thank You", "Admin Dashboard"])

# Session flag to show 'Thank You' after submit
if "submitted" not in st.session_state:
    st.session_state.submitted = False

with tab_feedback:
    st.header("📝 Share your feedback")
    st.write("We value your opinion. Please rate your experience and share any comments.")

    # Form
    with st.form("feedback_form", clear_on_submit=True):
        rating = st.slider("Overall rating", min_value=1, max_value=5, value=4, help="1 = Very poor, 5 = Excellent")
        category = st.text_input("Category (e.g., Product Quality, Support, Delivery)", value=categories_default[0])
        comments = st.text_area("Comments / Suggestions", height=120, placeholder="Tell us what went well or what we can improve.")
        st.markdown("**(Optional) Contact details**")
        cols = st.columns(3)
        with cols[0]:
            name = st.text_input("Name")
        with cols[1]:
            email = st.text_input("Email")
        with cols[2]:
            phone = st.text_input("Phone")

        consent = st.checkbox("I consent to store this feedback for quality improvement.", value=True)
        submitted = st.form_submit_button("Submit Feedback")

        if submitted:
            if not consent:
                st.warning("Please check the consent box to submit your feedback.")
            else:
                row = {
                    "timestamp": datetime.utcnow().isoformat(),
                    "rating": int(rating),
                    "category": category.strip(),
                    "comments": comments.strip(),
                    "name": name.strip(),
                    "email": email.strip(),
                    "phone": phone.strip(),
                }
                append_row(row)
                st.success("Thank you! Your feedback has been recorded.")
                st.session_state.submitted = True

with tab_thanks:
    st.header("🎉 Thank you!")
    if st.session_state.submitted:
        df_all = load_data()
        st.success("Your feedback was saved successfully.")
        st.write("Here's the current average rating from all customers:")
        st.subheader(star_display(avg_rating(df_all)))
        st.write("Recent feedback (latest 10):")
        st.dataframe(df_all.sort_values("timestamp", ascending=False).head(10), use_container_width=True, hide_index=True)
    else:
        st.info("Submit feedback in the first tab to see a confirmation here.")

with tab_admin:
    st.header("🔒 Admin Dashboard")
    if not admin_pin:
        st.info("Enter an Admin PIN in the sidebar to unlock the dashboard.")
    else:
        # In a real app you'd verify PIN against a secret; here any non-empty PIN enables the dashboard.
        df = load_data()
        if df.empty:
            st.warning("No feedback yet.")
        else:
            left, right = st.columns(2)
            with left:
                st.subheader("Overview")
                st.metric("Total feedback", len(df))
                st.metric("Average rating", f"{avg_rating(df):.2f} / 5")
                st.text(star_display(avg_rating(df)))
            with right:
                st.subheader("Export")
                csv = df.to_csv(index=False).encode("utf-8")
                st.download_button("⬇️ Download all feedback (CSV)", data=csv, file_name="feedback_data.csv", mime="text/csv")

            st.markdown("---")
            st.subheader("All feedback")
            st.dataframe(df.sort_values("timestamp", ascending=False), use_container_width=True, hide_index=True)

st.caption("Built with ❤️ using Streamlit")
