import pandas as pd
import streamlit as st
import altair as alt
import numpy as np


#========== Headers ==========
st.header('Random DataVisualization with Streamlit')
st.title('Streamlit Component Showcase')
st.subheader('Exploring Data with Streamlit')
st.caption('A simple example of using st.write with various data types')

#========== Text Outputs ==========
st.text("This is some raw text output.unformatted text.you can write normal sentences here.")
# ========== 🔢 LaTeX MATH ==========
st.latex(r"""
    E = mc^2 \\
    \int_0^\infty e^{-x^2} dx = \frac{\sqrt{\pi}}{2}
""")

# ========== 💻 DISPLAY CODE SNIPPETS ==========
st.code("""
# This is a Python code block
import numpy as np
np.random.randn(10, 3)
""", language='python')

# ========== 📊 DATAFRAME + MAGIC ==========
st.subheader("🔢 Random DataFrame (200 rows × 3 cols)")

df = pd.DataFrame(np.random.randn(200, 3), columns=["a", "b", "c"])
df  # <-- This is a "magic" command (same as st.write(df))

# ========== 📈 ALTAIR CHART ==========
st.subheader("📈 Altair Scatter Plot")

chart = alt.Chart(df).mark_circle().encode(
    x='a', 
    y='b',
    size='c', 
    color='c',
    tooltip=['a', 'b', 'c']
).interactive()

st.altair_chart(chart, use_container_width=True)

# ========== 🎯 BONUS: Custom Markdown ==========
st.markdown("""
### 🛠 Markdown Section
You can **bold**, *italicize*, and use bullet points:

- 📦 pandas for data
- 🎲 numpy for randomness
- 📈 altair for charts
- 🚀 streamlit for the app
""")

# ========== ✅ Ending Message ==========
st.success("You're now familiar with the core display functions of Streamlit! 🎉")
#st.failure("This is a failure message, just for demonstration purposes.")
st.info("This is an informational message to guide you through the app.")
st.write("This is a simple example of using st.write with various data types.")
st.write("You can also display text, numbers, dataframes, and charts using st.write.")
st.write("Enjoy exploring Streamlit's capabilities!")   

# ========== 📌 More Info with Expander ==========
with st.expander("ℹ️ Click here to learn about Magic Commands"):
    st.markdown("""
    Streamlit's **magic** lets you write variables or charts directly without using `st.write()`.

    ```python
    df  # magic
    ```

    is the same as:

    ```python
    st.write(df)
    ```
    """)