import streamlit as st
from datetime import datetime
import time

st.set_page_config(page_title="My First App", layout="centered")

st.title("Hello User!")
st.write("This is a basic Streamlit web app.")

# Live Clock Display
st.subheader("⏰ Current Time")
clock_placeholder = st.empty()
for _ in range(10):  # This loop limits the update to 10 seconds; change as needed
    current_time = datetime.now().strftime("%H:%M:%S")
    clock_placeholder.markdown(f"**{current_time}**")
    time.sleep(1)

# User Input
name = st.text_input("Enter your name:")
if name:
    st.success(f"Hello, {name} 👋")

# Footer
st.markdown("---")
st.markdown("Made with ❤️ by Aarav Shah")
