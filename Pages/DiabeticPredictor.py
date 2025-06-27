import streamlit as st
import time

def DiabetesPred(lst):
    import requests

    # NOTE: you must manually set API_KEY below using information retrieved from your IBM Cloud account (https://dataplatform.cloud.ibm.com/docs/content/wsj/analyze-data/ml-authentication.html)
    API_KEY = "xZTXObrkExtxVd0PT-NDspCGkVqXP1grM1KP6W84qSFv"
    token_response = requests.post('https://iam.cloud.ibm.com/identity/token', data={"apikey":
    API_KEY, "grant_type": 'urn:ibm:params:oauth:grant-type:apikey'})
    mltoken = token_response.json()["access_token"]

    header = {'Content-Type': 'application/json', 'Authorization': 'Bearer ' + mltoken}

    # NOTE: manually define and pass the array(s) of values to be scored in the next line
    payload_scoring = {"input_data": [{"field": [["Pregnancies", "Glucose", "BloodPressure", "SkinThickness", "Insulin", "BMI", "DiabetesPedigreeFunction", "Age"]], "values": [lst]}]}

    response_scoring = requests.post('https://us-south.ml.cloud.ibm.com/ml/v4/deployments/10e06046-613b-4cc6-bac1-cb3d5e330527/predictions?version=2021-05-01', json=payload_scoring,
     headers={'Authorization': 'Bearer ' + mltoken})
    print("Scoring response")
    predictions = response_scoring.json()
    pred = predictions['predictions'][0]['values'][0][0]
    if (pred == 1):
        return "You are Diabetic"
    else:
        return "You are not Diabetic"
        
        
st.markdown("""
<style>
.st-emotion-cache-czk5ss.e16jpq800{
    visibility: hidden;
}
.st-emotion-cache-mnu3yk.ef3psqc5{
    visibility: hidden;
}
.st-emotion-cache-15ecox0.ezrtsby0{
    visibility: hidden;
}

</style>            
""", unsafe_allow_html=True)
st.link_button("HomePage", "https://techtitans.streamlit.app/")


st.markdown("<h1 style='text-align: center;'>Diabetes Predictor</h1>",unsafe_allow_html=True)
with st.form("Form 1"):
    col1,col2,col3,col4=st.columns(4)
    Pregnancies=col1.number_input("Pregnancies",format="%.0f")
    Glucose=col2.number_input("Glucose",format="%.0f")
    BloodPressure=col3.number_input("BloodPressure",format="%.0f")
    SkinThickness=col4.number_input("SkinThickness",format="%.0f")
    col5,col6,col7,col8=st.columns(4)
    Insulin=col5.number_input("Insulin",format="%.0f")
    BMI=col6.number_input("BMI")
    DiabetesPedigreeFunction=col7.number_input("DiabetesPedigreeFunction")
    Age=col8.number_input("Age",format="%.0f")
    lst = [Pregnancies,Glucose,BloodPressure,SkinThickness,Insulin,BMI,DiabetesPedigreeFunction,Age]
    submit = st.form_submit_button('Predict')  
    
    if submit:
        progress_text = "Operation in progress. Please wait."
        my_bar = st.progress(0, text=progress_text)

        for percent_complete in range(100):
            time.sleep(0.6)
            my_bar.progress(percent_complete + 1, text=progress_text)
        time.sleep(1)
        my_bar.empty()
        st.text_area(label ="Model Prediction",value=DiabetesPred(lst), height =100)
    
