import streamlit as st

with st.echo():
    st.write("Hello, this is inside st.echo()")
    x = 10 * 2
    st.write("Result is:", x)

