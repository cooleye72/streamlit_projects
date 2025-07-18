import streamlit as st
import pandas as pd
import numpy as np

st.title('About this App')
st.write('This is a Streamlit app that demonstrates how to handle user queries and generate responses based on course details.')
with st.expander("How to use App"):
    st.write("1. Enter your prompt in the text area.\n 2. Click the Submit button.\n 3. The app will generate a text completion based on your prompt.")