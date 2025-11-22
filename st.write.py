''' In Streamlit, we use st.write() to show or display any output on the web page.
It is very flexible and works for text, tables, images, charts, and even DataFrames'''

### 🗯️ Show anything? — st.write()




import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt 

# 1️⃣ Create simple table (DataFrame)

data = {'name':['nani','bunny','sunny'],
        'age':[23,25,27],
        'address':['hyd','chennai','bglr']}
df = pd.DataFrame(data)

st.write('address of the people')
st.write(df)

# 2️⃣ Create a simple Matplotlib line chart

fig,ax = plt.subplots()
ax.plot(df['name'],df['age'])
ax.set_title('student marks')
ax.set_xlabel('name')
ax.set_ylabel('age')

st.write(fig)
