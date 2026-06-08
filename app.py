import pandas as pd
import streamlit as st
import plotly.express as px

# Sample Data
df = pd.DataFrame({
    "Month": ["Jan", "Feb", "Mar", "Apr", "May"],
    "Sales": [100, 150, 120, 180, 200],
    "Revenue": [10000, 15000, 12000, 18000, 20000]
})

# Dashboard Title
st.title("Sales & Revenue Analysis Dashboard")

# KPIs
st.subheader("Key Performance Indicators")
st.write("Total Sales:", df["Sales"].sum())
st.write("Total Revenue: ₹", df["Revenue"].sum())

# Sales Trend Chart
st.subheader("Sales Trend")
fig1 = px.line(df, x="Month", y="Sales", markers=True)
st.plotly_chart(fig1)

# Revenue Trend Chart
st.subheader("Revenue Trend")
fig2 = px.bar(df, x="Month", y="Revenue")
st.plotly_chart(fig2)

# Data Table
st.subheader("Sales Data")
st.dataframe(df)
