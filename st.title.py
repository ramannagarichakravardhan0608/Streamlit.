import streamlit as st

# Main Title of the app
st.title("📘 Student Report Web App")

# Header (Section title)
st.header("📊 Marks Overview")

# Subheader (Smaller section)
st.subheader("Top Students")

# Plain text (no style)
st.text("This is a simple Streamlit app to show student marks.")

# Markdown (Styled text)
st.markdown("**Here is a bold line using st.markdown()**")
st.markdown("*Here is an italic line*")
st.markdown("- Apple 🍎 \n- Banana 🍌 \n- Mango 🥭")
st.markdown("[Visit Google](https://www.google.com)")