import streamlit as st
from datetime import datetime
import pytz
from streamlit_autorefresh import st_autorefresh

# Page setup
st.set_page_config(page_title="World Clock", layout="centered")

# Auto-refresh every 1 second
st_autorefresh(interval=1000, limit=None, key="auto_refresh")

st.title("🌍 World Clock")

# --- Country to timezone mapping ---
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
}

# --- User selections ---
st.sidebar.header("Settings")

country = st.sidebar.selectbox("Select your country:", list(country_timezone_map.keys()))
time_format = st.sidebar.radio("Select time format:", ["24-hour", "12-hour"])

# Store selections
st.session_state["timezone"] = country_timezone_map[country]
st.session_state["format_24hr"] = time_format == "24-hour"

# --- Time Display ---
st.subheader(f"🕒 Current Time in {country}")
tz = pytz.timezone(st.session_state["timezone"])
now = datetime.now(tz)

if st.session_state["format_24hr"]:
    formatted_time = now.strftime("%Y-%m-%d %H:%M:%S")
else:
    formatted_time = now.strftime("%Y-%m-%d %I:%M:%S %p")

st.markdown(f"### {formatted_time}")

# --- Footer ---
st.markdown("---")
st.markdown("*Built with Streamlit*")
