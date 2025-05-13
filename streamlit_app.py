import streamlit as st

st.set_page_config(page_title="My First App", layout="centered")

st.title("🎈 Hello Streamlit!")
st.write("This is a basic Streamlit web app.")

name = st.text_input("Enter your name:")
if name:
    st.success(f"Hello, {name} 👋")
    # --- Footer ---
st.markdown("""
<hr style="margin-top: 2em; margin-bottom: 1em;">

<div style='text-align: center; color: gray;'>
    Made with ❤️ by Aarav Shah
</div>
""", unsafe_allow_html=True)
