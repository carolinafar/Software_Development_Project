"""
Streamlit app for visualizing car sales data
"""

import pandas as pd
import streamlit as st
import plotly.express as px

df = pd.read_csv('notebooks/vehicles_us.csv')

old_cars_odometer_filter = (df['model_year'] >= 1969) | (df['odometer'] <= 100000)

high_mileage_filter = df['odometer'] <= 400000

cars_under_100k_filter = df['price'] <= 100000

odometer_non_null_filter = df['odometer'].notna()

df_cleaned = df[old_cars_odometer_filter &
                high_mileage_filter &
                cars_under_100k_filter &
                odometer_non_null_filter]

st.header("Analysis of Vehicle Dataset")

# Checkbox for filtering data
filter_data = st.checkbox("Filter Data by Car Model")
if filter_data:
    car_model = st.selectbox(
        "Select Car Model:",
        options=df_cleaned['model'].unique())
    filtered_data = df_cleaned[df_cleaned['model'] == car_model]
else:
    filtered_data = df_cleaned

# Checkbox for Odometer Distribution Histogram
show_odometer_hist = st.checkbox("Show Odometer Distribution Histogram")
if show_odometer_hist:
    fig_odometer = px.histogram(filtered_data, x='odometer', title="Odometer Distribution")
    fig_odometer.update_yaxes(title="Count", dtick=1000, showgrid=True)  # Show grid lines
    st.plotly_chart(fig_odometer)

# Checkbox for Price vs Model Year Scatter Plot
show_scatter_plot = st.checkbox("Show Price vs Model Year Scatter Plot")
if show_scatter_plot:
    fig_scatter = px.scatter(filtered_data, x='model_year', y='price', title='Price vs Model Year')
    fig_scatter.update_layout(xaxis_title='Model Year', yaxis_title='Price')
    st.plotly_chart(fig_scatter)

# Checkbox for Price Distribution Histogram
show_price_hist = st.checkbox("Show Price Distribution Histogram")
if show_price_hist:
    fig_price = px.histogram(filtered_data, x='price', title="Price Distribution")
    fig_price.update_xaxes(title="Price", tickformat=",")  # Use thousands separators on x-axis
    fig_price.update_yaxes(title="Count", tickformat=",")  # Use thousands separators on y-axis
    st.plotly_chart(fig_price)
