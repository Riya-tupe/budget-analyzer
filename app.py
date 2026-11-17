# Project: Smart Budget & Expense Analyzer
# Subject: Linear Algebra & Matrix Application Mini Project
# Developed by: Student

import streamlit as st
import numpy as np

# Page configuration
st.set_page_config(page_title="Budget Analyzer", page_icon="💰")

st.title("Smart Budget & Expense Analyzer")
st.write("Hello! This tool helps to calculate and manage monthly expenses and savings using simple array calculations.")

# Taking income input from user
st.markdown("### 1. Enter Your Income")
my_income = st.number_input("Monthly Income (in ₹):", min_value=0.0, value=25000.0, step=1000.0)

# Taking expenses for different categories
st.markdown("### 2. Enter Your Expenses")
food_exp = st.number_input("Food Expense", min_value=0.0, value=4000.0)
rent_exp = st.number_input("Rent Expense", min_value=0.0, value=0.0)
bills_exp = st.number_input("Bills Expense", min_value=0.0, value=2000.0)
travel_exp = st.number_input("Travel Expense", min_value=0.0, value=2000.0)
fun_exp = st.number_input("Fun & Leisure Expense", min_value=0.0, value=4000.0)

# Storing expenses in a numpy array (as learned in Linear Algebra / Arrays)
category_names = ["Food", "Rent", "Bills", "Travel", "Fun"]
expense_values = np.array([food_exp, rent_exp, bills_exp, travel_exp, fun_exp], dtype=float)

# Basic calculations using numpy functions
total_expense_amount = np.sum(expense_values)
total_savings = my_income - total_expense_amount

# Displaying final results
st.markdown("---")
st.markdown("### 3. Final Calculation Result")

col1, col2, col3 = st.columns(3)
col1.metric("Total Income", f"₹ {my_income}")
col2.metric("Total Expense", f"₹ {total_expense_amount}")
col3.metric("Total Savings", f"₹ {total_savings}")

# Simple decision making logic for analysis
if np.sum(expense_values) > 0:
    max_index = np.argmax(expense_values)
    st.info(f"Analysis Note: Your highest spending category is **{category_names[max_index]}** with an amount of ₹{expense_values[max_index]}.")

if total_savings > 10000:
    st.success("Result: Excellent savings management! Keep it up.")
elif total_savings > 0:
    st.warning("Result: Moderate savings. Try to cut down on extra expenses.")
else:
    st.error("Alert: Expenses are higher than your income!")
