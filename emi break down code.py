# -*- coding: utf-8 -*-
"""
Created on Thu Jul 24 18:59:03 2025

@author: bhara
"""

car_price = 1400000       # Total price of the car
down_payment = 140000     
loan_amount = car_price - down_payment
# EMI Calculator for Car Loan
annual_interest_rate = 12  # percent
loan_tenure_years = 7
months = loan_tenure_years * 12
monthly_interest_rate = annual_interest_rate / (12 * 100)  # Convert annual rate to monthly decimal

# EMI Calculation
emi = loan_amount * monthly_interest_rate * ((1 + monthly_interest_rate) ** months) / ((1 + monthly_interest_rate) ** months - 1)

# Output
print(f"Car Price    : Rs.{car_price}")
print(f"Down Payment : Rs.{down_payment}")
print(f"Loan Amount  : Rs.{loan_amount}")
print(f"Interest Rate: {annual_interest_rate}% per year")
print(f"Loan Tenure  : {loan_tenure_years} years")
print(f"Monthly EMI  : Rs.{emi}")