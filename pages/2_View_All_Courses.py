import streamlit as st
import json
import pandas as pd
import numpy as np

filepath = './data/courses-full.json'
# filepath = 'courses-full.json'

st.title("View All Courses")
with open(filepath, 'r') as file:
    json_string = file.read()
    dict_of_courses = json.loads(json_string)
    
df = pd.DataFrame(dict_of_courses)
# Rotate (transpose) the DataFrame
df_rotated = df.T

df_rotated.reset_index(drop=True, inplace=True)


st.dataframe(df_rotated)