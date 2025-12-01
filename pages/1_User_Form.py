# User Input: Form

import streamlit as st
import pickle
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import warnings
warnings.filterwarnings("ignore")


# Set up the title and description of the app
st.markdown("<h1 style='text-align: center;'>Fill Out the Credit Card Survey</h1>", unsafe_allow_html=True) 

features = ['Applicant_Gender', 'Owned_Car', 'Owned_Realty',
            'Total_Children', 'Total_Income', 'Income_Type', 'Education_Type',
            'Family_Status', 'Housing_Type', 'Owned_Mobile_Phone',
            'Owned_Work_Phone', 'Owned_Phone', 'Owned_Email', 'Job_Title',
            'Total_Family_Members', 'Applicant_Age', 'Years_of_Working',
            'Total_Bad_Debt', 'Total_Good_Debt']

st.markdown("<p style='text-align: center;'>Fill out the form to predict whether you'll be approved for a credit card.</p>", unsafe_allow_html=True)

with st.form("user_inputs_form"):

    st.subheader("Part 1: Personal Details")
    applicant_gender = st.radio(
        "Applicant Gender",
        options=["Male", "Female"],
        index=0 if st.session_state.get('Applicant_Gender', "Male") == "Male" else 1
    )

    applicant_age = st.number_input(
        "Applicant Age",
        min_value=18,
        value=st.session_state.get('Applicant_Age', 30)
    )

    st.subheader("Part 2: Employment Details")
    job_title_options = [
        'Security staff', 'Sales staff', 'Accountants', 'Laborers', 'Managers', 'Drivers', 
        'Core staff', 'High skill tech staff', 'Cleaning staff', 'Private service staff',
        'Cooking staff', 'Low-skill Laborers', 'Medicine staff', 'Secretaries', 'Waiters/barmen staff',
        'HR staff', 'Realty agents', 'IT staff'
    ]

    job_title = st.selectbox(
        "What is your job title?",
        options=job_title_options,
        index=job_title_options.index(st.session_state.get('Job_Title', 'Core staff'))
    )

    years_of_working = st.number_input(
        "How many years have you worked?",
        min_value=0,
        value=st.session_state.get('Years_of_Working', 5)
    )

    income_type_options = [
        'Working', 'Commercial associate', 'State servant', 'Student', 'Pensioner'
    ]

    income_type = st.selectbox(
        "Income Type",
        options=income_type_options,
        index=income_type_options.index(st.session_state.get('Income_Type', 'Working')),
        help = "Where income is coming from"
    )

    education_options = ['Higher education','Secondary / secondary special','Incomplete higher', 'Lower secondary','Academic degree']
    
    education_type = st.selectbox(
        "Education Level",
        options=education_options,
        index=education_options.index(st.session_state.get('Education_Type', 'Higher education'))
    )

    total_income = st.number_input(
        "Total Income",
        min_value=0,
        value=st.session_state.get('Total_Income', 50000)
    )

    st.subheader("Part 3: Household Information")
    owned_car = st.radio(
        "Do you own a car?",
        options=["Yes", "No"],
        index=0 if st.session_state.get('Owned_Car', 0) == 1 else 1
    )

    owned_realty = st.radio(
        "Do you own realty/property?",
        options=["Yes", "No"],
        index=0 if st.session_state.get('Owned_Realty', 0) == 1 else 1
    )

    total_children = st.number_input(
        "How many children do you have?",
        min_value=0,
        max_value=5,
        value=st.session_state.get('Total_Children', 0)
    )

    total_family_members = st.number_input(
        "How many family members do you have?",
        min_value=1,
        value=st.session_state.get('Total_Family_Members', 1)
    )

    family_status_options = [
        'Married', 'Single / not married', 'Civil marriage', 'Separated', 'Widow'
    ]

    family_status = st.selectbox(
        "Marriage Status",
        options=family_status_options,
        index=family_status_options.index(st.session_state.get('Family_Status', 'Single / not married'))
    )

    housing_type_options = [
        'House / apartment', 'Rented apartment', 'Municipal apartment', 'With parents', 'Co-op apartment', 'Office apartment'
    ]

    housing_type = st.selectbox(
        "Housing Type",
        options=housing_type_options,
        index=housing_type_options.index(st.session_state.get('Housing_Type', 'House / apartment')),
        help = "Type of housing where the applicant lives"
    )

    owned_work_phone = st.radio(
        "Do you own a work phone?",
        options=["Yes", "No"],
        index=0 if st.session_state.get('Owned_Work_Phone', 0) == 1 else 1
    )

    owned_phone = st.radio(
        "Do you own any phone?",
        options=["Yes", "No"],
        index=0 if st.session_state.get('Owned_Phone', 0) == 1 else 1
    )

    owned_email = st.radio(
        "Do you have an email?",
        options=["Yes", "No"],
        index=0 if st.session_state.get('Owned_Email', 0) == 1 else 1
    )

    st.subheader("Part 4: Financial Obligations")
    total_bad_debt = st.number_input(
        "Total Bad Debt",
        min_value=0,
        value=st.session_state.get('Total_Bad_Debt', 0),
        help = "Amount of debt that is overdue (Ex. Overdue loans)"
    )

    total_good_debt = st.number_input(
        "Total Good Debt",
        min_value=0,
        value=st.session_state.get('Total_Good_Debt', 0),
        help = "Amount of debt that is being managed and paid on time (Ex. Mortgage, student loans)"
    )

    submit_button = st.form_submit_button("Submit")

# # Save the inputs to session state if the form is submitted
if submit_button:
    st.session_state['Applicant_Gender'] = "M" if applicant_gender == "Male" else "F"
    st.session_state['Applicant_Age'] = applicant_age
    st.session_state['Job_Title'] = job_title
    st.session_state['Years_of_Working'] = years_of_working
    st.session_state['Income_Type'] = income_type
    st.session_state['Total_Income'] = total_income
    st.session_state['Education_Type'] = education_type
    st.session_state['Owned_Car'] = 1 if owned_car == "Yes" else 0
    st.session_state['Owned_Realty'] = 1 if owned_realty == "Yes" else 0
    st.session_state['Total_Children'] = total_children
    st.session_state['Total_Family_Members'] = total_family_members
    st.session_state['Family_Status'] = family_status
    st.session_state['Housing_Type'] = housing_type
    st.session_state['Owned_Work_Phone'] = 1 if owned_work_phone == "Yes" else 0
    st.session_state['Owned_Phone'] = 1 if owned_phone == "Yes" else 0
    st.session_state['Owned_Email'] = 1 if owned_email == "Yes" else 0
    st.session_state['Total_Bad_Debt'] = total_bad_debt
    st.session_state['Total_Good_Debt'] = total_good_debt
    st.session_state['form_submitted'] = True

    st.success("✅ Your survey responses have been saved!")

else:
    st.warning("⚠️ Fill out the form and click Submit..")