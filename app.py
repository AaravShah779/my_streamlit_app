import streamlit as st
from datetime import datetime
import pytz
import time

st.set_page_config(
    page_title="World Clock",
    layout="centered",
)

# Sidebar controls
country_timezone_map = {
    "India": "Asia/Kolkata",
    "United States (Eastern)": "US/Eastern",
    "United States (Pacific)": "US/Pacific",
    "United Kingdom": "Europe/London",
    "Germany": "Europe/Berlin",
    "Japan": "Asia/Tokyo",
    "Australia": "Australia/Sydney",
    "Brazil": "America/Sao_Paulo",
    "UAE": "Asia/Dubai",
    "South Africa": "Africa/Johannesburg",
    "China": "Asia/Shanghai",
    "Russia (Moscow)": "Europe/Moscow",
    "France": "Europe/Paris",
    "Canada (Eastern)": "Canada/Eastern",
    "Mexico": "America/Mexico_City",
}

# Theme selector
theme = st.sidebar.radio("Select Theme:", ["Light", "Dark"])

# Country selector
country = st.sidebar.selectbox("Select Country:", list(country_timezone_map.keys()))

# Time format selector
time_format = st.sidebar.radio("Select Time Format:", ["24-hour", "12-hour"])

# Apply styles based on theme
if theme == "Dark":
    st.markdown(
        """
        <style>
        body, .css-18e3th9 {background-color: #0e1117; color: white;}
        .stButton>button {background-color: #1e2127; color: white;}
        </style>
        """,
        unsafe_allow_html=True,
    )
else:
    st.markdown(
        """
        <style>
        body, .css-18e3th9 {background-color: white; color: black;}
        .stButton>button {background-color: #f0f2f6; color: black;}
        </style>
        """,
        unsafe_allow_html=True,
    )

st.title("🌍 World Clock")

# Container to hold the live clock
clock_placeholder = st.empty()

tz = pytz.timezone(country_timezone_map[country])

def get_current_time():
    now = datetime.now(tz)
    if time_format == "24-hour":
        return now.strftime("%Y-%m-%d %H:%M:%S")
    else:
        return now.strftime("%Y-%m-%d %I:%M:%S %p")

# Live updating clock loop (will update for 1 minute)
for _ in range(60):
    current_time = get_current_time()
    clock_placeholder.markdown(f"### Current time in **{country}**")
    clock_placeholder.markdown(f"<h2 style='font-weight:600;'>{current_time}</h2>", unsafe_allow_html=True)
    time.sleep(1)

# Footer
st.markdown("---")
st.markdown("<p style='text-align:center;'>Made with ❤️ by Aarav Shah</p>", unsafe_allow_html=True)
