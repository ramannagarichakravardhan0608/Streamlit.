import streamlit as st

code = """
import pandas as pd
df = pd.read_csv("data.csv")
st.write(df)
df.fillna(df[chakravardhan].median)
"""

st.code(code, language="python")
