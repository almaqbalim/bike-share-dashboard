import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

# ─────────────────────────────────────
# 🔧 Config & Styling
# ─────────────────────────────────────
st.set_page_config(page_title="Cyclistic Bike-Share Report", layout="wide")
sns.set_style("whitegrid")
plt.rcParams["axes.facecolor"] = "white"
plt.rcParams["figure.facecolor"] = "white"

# Fixed color scheme
user_colors = {
    "casual": "#E76F51",
    "member": "#2A9D8F"
}

# ─────────────────────────────────────
# 📥 Load Data
# ─────────────────────────────────────


@st.cache_data
def load_data():
    df = pd.read_csv("https://huggingface.co/datasets/almaqbalim/BikeShare/resolve/main/dataset.csv")
    df['started_at'] = pd.to_datetime(df['started_at'])
    df['ended_at'] = pd.to_datetime(df['ended_at'])
    df['ride_length'] = (df['ended_at'] - df['started_at']
                         ).dt.total_seconds() / 60
    df['month'] = df['started_at'].dt.month_name()
    df['day_of_week'] = df['started_at'].dt.day_name()
    df['hour'] = df['started_at'].dt.hour
    return df


df = load_data()

# ─────────────────────────────────────
# 📘 Header
# ─────────────────────────────────────

st.title("🚲 Cyclistic Bike-Share Report")
st.markdown("**Prepared by Mohammed Almaqbali**")

st.markdown("---")

# ─────────────────────────────────────
# 🧾 Executive Summary
# ─────────────────────────────────────
st.markdown("### 📊 Executive Summary")
st.info(
    "This dashboard explores behavioral patterns of Cyclistic riders, comparing casual vs. member usage across time, trip length, and volume."
)

# ─────────────────────────────────────
# 📁 Dataset Overview
# ─────────────────────────────────────
st.markdown("### 📁 Dataset Overview")
st.write(f"**Total rides:** {df.shape[0]:,}")
st.write(
    f"**Date range:** {df['started_at'].min().date()} → {df['started_at'].max().date()}")
st.write(f"**User types:** {', '.join(df['member_casual'].unique())}")

# ─────────────────────────────────────
# 🧑‍🤝‍🧑 User Type Pie & Duration
# ─────────────────────────────────────
col1, col2 = st.columns(2)

with col1:
    st.markdown("#### 🧑‍🤝‍🧑 User Type Distribution")
    user_counts = df['member_casual'].value_counts()
    fig, ax = plt.subplots(figsize=(4, 3), dpi=150)
    ax.pie(user_counts, labels=user_counts.index, autopct='%1.1f%%',
           colors=[user_colors[i] for i in user_counts.index], explode=[0.05, 0.05], shadow=True)
    ax.axis('equal')
    fig.tight_layout()
    st.pyplot(fig)

with col2:
    st.markdown("#### ⏱️ Average Trip Duration")
    duration_stats = df.groupby('member_casual')['ride_length'].mean().round(1)
    fig, ax = plt.subplots(figsize=(4, 3), dpi=150)
    ax.bar(duration_stats.index, duration_stats.values,
           color=[user_colors[i] for i in duration_stats.index])
    ax.set_ylabel("Minutes")
    ax.set_title("Avg. Trip Duration")
    fig.tight_layout()
    st.pyplot(fig)

# ─────────────────────────────────────
# 📅 Monthly Trends & 📆 Weekly Trends
# ─────────────────────────────────────
col3, col4 = st.columns(2)

with col3:
    st.markdown("#### 📅 Monthly Trip Volume")
    monthly_counts = df.groupby(['month', 'member_casual']).size().unstack().reindex([
        'January', 'February', 'March', 'April', 'May', 'June',
        'July', 'August', 'September', 'October', 'November', 'December'
    ])
    fig, ax = plt.subplots(figsize=(5, 3), dpi=150)
    monthly_counts.plot(kind='bar', ax=ax,
                        color=[user_colors[col] for col in monthly_counts.columns])
    ax.set_ylabel("Trips")
    ax.set_xlabel("")
    ax.set_title("Trips by Month")
    fig.tight_layout()
    st.pyplot(fig)

with col4:
    st.markdown("#### 📆 Weekly Ride Patterns")
    weekday_order = ['Monday', 'Tuesday', 'Wednesday',
                     'Thursday', 'Friday', 'Saturday', 'Sunday']
    weekday_counts = df.groupby(
        ['day_of_week', 'member_casual']).size().unstack().reindex(weekday_order)
    fig, ax = plt.subplots(figsize=(5, 3), dpi=150)
    weekday_counts.plot(kind='bar', ax=ax,
                        color=[user_colors[col] for col in weekday_counts.columns])
    ax.set_ylabel("Trips")
    ax.set_title("Trips by Day of the Week")
    fig.tight_layout()
    st.pyplot(fig)

# ─────────────────────────────────────
# ⏰ Hourly Patterns (Full Width)
# ─────────────────────────────────────
st.markdown("#### ⏰ Hourly Ride Trends")
hourly_counts = df.groupby(['hour', 'member_casual']).size().unstack()
fig, ax = plt.subplots(figsize=(8, 3), dpi=150)
hourly_counts.plot(ax=ax, marker='o',
                   color=[user_colors[col] for col in hourly_counts.columns])
ax.set_xlabel("Hour")
ax.set_ylabel("Trips")
ax.set_title("Trips by Hour of Day")
fig.tight_layout()
st.pyplot(fig)

# ─────────────────────────────────────
# 🔍 Insights & 💡 Recommendations
# ─────────────────────────────────────
st.markdown("### 🔍 Key Insights")
st.success("""
- Casual users ride longer and mostly on weekends (midday peak)  
- Members ride frequently on weekdays during commute hours  
- Demand surges during summer (especially July–August)
""")

st.markdown("### 💡 Strategic Recommendations")
st.warning("""
- Convert casuals with trial/weekend memberships  
- Increase bike availability during peak hours and in parks  
- Promote convenience, savings, and loyalty benefits of membership
""")

# ─────────────────────────────────────
# 🔗 GitHub Project Link
# ─────────────────────────────────────
st.markdown("### 📂 Project Repository")
st.markdown(
    "All source files and documentation are available on GitHub:\n\n"
    "[View Project on GitHub](https://github.com/almaqbalim/bike-share-dashboard)"
)

# ─────────────────────────────────────
# 📘 Footer
# ─────────────────────────────────────
st.markdown("---")
st.markdown("📘 Report created by **Mohammed Almaqbali** | Powered by Streamlit")
