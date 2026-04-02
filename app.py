import streamlit as st
import joblib
import pandas as pd
import numpy as np

#Load the model and label encoder
model = joblib.load(r'C:\Users\Vyshnavi bijili\OneDrive\Documents\GitHub\desktop1\project1\attrition_model.pkl')
label_encoder = joblib.load(r'C:\Users\Vyshnavi bijili\OneDrive\Documents\GitHub\desktop1\project1\label_encoder.pkl')
feature_columns = joblib.load(r'C:\Users\Vyshnavi bijili\OneDrive\Documents\GitHub\desktop1\project1\feature_columns.pkl')

st.title("Employee Prediction ")

st.markdown("Enter the employee details to predict if they are"
            "likely to leave the company.")

# function to grt user input for prediction
st.sidebar.header("Employee Details")

def get_user_input():
    inputs = {}
    inputs['Age'] = st.sidebar.number_input("Age", min_value=18, max_value=65, value=30)
    inputs['MonthlyIncome'] = st.sidebar.number_input("MonthlyIncome", min_value=1000, max_value=20000, value=5000)
    inputs['JobSatisfaction']=st.sidebar.selectbox("JobSatisfaction",options=[1,2,3,4])
    inputs['OverTime']=st.sidebar.selectbox("OverTime",options=["Yes","No"])
    inputs['DistanceFromHome']=st.sidebar.number_input("DistanceFromHome",min_value=0,max_value=50,value=10)
    
    data={}
    for feat in feature_columns:
        if feat in inputs:
            data[feat]=inputs[feat]
        else:
            data[feat]=0
    return pd.DataFrame(data,index=[0])


user_input=get_user_input()

user_input['OverTime'] = label_encoder.fit_transform(user_input['OverTime'])

if st.button("Prediction Attrition"):
    prediction=model.predict(user_input)
    if prediction[0]==1:
        st.error("The employee is likely to leave the company")
    else:
        st.success("The employee is likely to stay in the company")