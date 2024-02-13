import numpy as np
import pandas as pd
import plotly.express as px
import streamlit as st
import data_analysis as da
import glob
import anomalies_identification as ai


# Define the directory path
data_dir = "dataset/real_test_case"

# Get a list of all CSV files matching the pattern
file_paths = glob.glob(data_dir + '/*.csv')

# Read data
dfs = [pd.read_csv(file) for file in file_paths]
real_test_case = pd.concat(dfs, ignore_index=True)

real_test_case = ai.data_preprocessing(real_test_case)

# Calculate store daily visits
store_daily_visits = da.calculate_store_daily_visits(real_test_case)


st.markdown("<h2 class='title'>Pick a Date</h2>", unsafe_allow_html=True)
selected_date = st.date_input("", key="date_input")
st.markdown("<style>.css-1v3fvcr {text-align: center;}</style>", unsafe_allow_html=True)

if selected_date:
        selected_date_str = selected_date.strftime("%Y-%m-%d")
        visit_count_row = store_daily_visits[store_daily_visits['visits_date'] == selected_date_str]
        if not visit_count_row.empty:
            visits_count = visit_count_row.iloc[0]['store_daily_visits']
            st.write(f"Store daily visits count for {selected_date_str}: {visits_count}")
        else:
            st.write(f"No data available for {selected_date_str}")
