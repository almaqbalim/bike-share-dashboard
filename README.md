# 🚲 Cyclistic Bike-Share Data Analysis

This project presents an in-depth analysis of a year's worth of bike-share data from **Cyclistic**, a fictional bike-share company. The goal is to understand how different types of users (casual vs. members) behave, and provide data-driven insights to improve membership conversion and operational strategy.

---

## 📊 Project Overview

This interactive dashboard was built using **Python**, **Pandas**, **Matplotlib**, **Seaborn**, and **Streamlit**. It compares user behavior across dimensions such as:

- 📅 Monthly ride volume
- 📆 Day-of-week patterns
- ⏰ Hourly ride trends
- 🧑‍🤝‍🧑 User type distribution
- ⏱️ Average ride duration

---

## 📂 Files Included

| File | Description |
|------|-------------|
| `app.py` | Streamlit dashboard code |
| `dataset.csv` | Cleaned and prepared dataset |
| `Analyze_bike_share_data.ipynb` | Original Jupyter Notebook analysis |
| `logo.jpg` | Branding/logo for the dashboard |
| `README.md` | This file |

---

## 📈 Key Findings

- **Casual riders** take longer trips, mainly on **weekends** during **midday** hours.
- **Members** ride more frequently, especially on **weekdays** and **commute hours (4–6 PM)**.
- **Summer months** (July–August) see the highest usage for both rider types.

---

## 💡 Recommendations

- 🎯 Offer **trial or weekend-based memberships** to attract casual riders.
- 🚲 Increase bike availability during **commute hours** and in **leisure areas**.
- 📣 Promote **cost efficiency and convenience** of annual membership through in-app campaigns.

---

## 🌐 Live Demo

You can explore the interactive dashboard by launching the app locally or deploying it on [Streamlit Cloud](https://streamlit.io/).

```bash
streamlit run app.py
