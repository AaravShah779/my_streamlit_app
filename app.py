import streamlit as st
from datetime import datetime
import pytz
import time

st.set_page_config(page_title="My First App", layout="centered")

st.title("🎈 Hello Streamlit!")
st.write("This is a basic Streamlit web app.")

# --- Timezone selection ---
st.subheader("⏰ Current Time")

# Available timezones
timezones = ['Asia/Kolkata', 'UTC', 'US/Eastern', 'Europe/London', 'Asia/Tokyo', 'Australia/Sydney']
default_tz = 'Asia/Kolkata'  # IST
selected_tz = st.selectbox("Select a timezone:", timezones, index=timezones.index(default_tz))

# Display current time in selected timezone
clock_placeholder = st.empty()

for _ in range(10):  # Updates every second for 10 seconds
    tz = pytz.timezone(selected_tz)
    current_time = datetime.now(tz).strftime("%Y-%m-%d %H:%M:%S")
    clock_placeholder.markdown(f"**Current Time in {selected_tz}:** {current_time}")
    time.sleep(1)

# --- User Input ---
name = st.text_input("Enter your name:")
if name:
    st.success(f"Hey, {name} 👋")

# --- Footer ---
st.markdown("---")
st.markdown("Made with ❤️ by Aarav Shah")
