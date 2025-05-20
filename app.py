import streamlit as st
from datetime import datetime
import pytz

# Page config with dynamic theme
st.set_page_config(
    page_title="World Clock",
    layout="centered",
)

# Light/Dark mode toggle
theme = st.sidebar.radio("Select Theme:", ["Light", "Dark"])
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

# List of countries and their main timezones
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

# Sidebar controls
country = st.sidebar.selectbox("Select Country:", list(country_timezone_map.keys()))
time_format = st.sidebar.radio("Select Time Format:", ["24-hour", "12-hour"])

# Fetch current time in chosen timezone
tz = pytz.timezone(country_timezone_map[country])
now = datetime.now(tz)

if time_format == "24-hour":
    current_time = now.strftime("%Y-%m-%d %H:%M:%S")
else:
    current_time = now.strftime("%Y-%m-%d %I:%M:%S %p")

st.markdown(f"### Current time in **{country}**")
st.markdown(f"<h2 style='font-weight:600;'>{current_time}</h2>", unsafe_allow_html=True)

# Footer
st.markdown("---")
st.markdown("<p style='text-align:center;'>Made with ❤️ by Aarav Shah</p>", unsafe_allow_html=True)
