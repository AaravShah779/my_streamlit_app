import streamlit as st
import streamlit.components.v1 as components

st.title("🌍 Simple Rotating Globe")

country_coords = {
    "India": [78.9629, 20.5937],
    "United States (Eastern)": [-75.1652, 39.9526],
    "United States (Pacific)": [-122.4194, 37.7749],
    "United Kingdom": [-0.1276, 51.5074],
    "Germany": [13.4050, 52.5200],
    "Japan": [139.6917, 35.6895],
    "Australia": [151.2093, -33.8688],
    "Brazil": [-47.8825, -15.7942],
    "UAE": [54.3773, 24.4539],
    "South Africa": [28.0473, -26.2041],
}

country = st.selectbox("Select Country:", list(country_coords.keys()))

st.markdown(f"Selected country: **{country}**")

# Read the globe html file and embed it
with open("globe.html", "r") as f:
    globe_html = f.read()

components.html(globe_html, height=600)

# --- Footer ---
st.markdown("---")
st.markdown("*Built with Streamlit*")
