import streamlit as st
import time

def ecg(n):
    if n == "Normal":
        return 0
    elif n == "Having ST-T wave abnormality (T wave inversions and/or ST elevation or depression of > 0.05 mV)":
        return 1
    elif n == "Showing probable or definite left ventricular hypertrophy by Estes' criteria":
        return 2
def YN(n):
    if n == "Yes":
        return 1
    else:
        return 0
def MF(n):
    if n=="Female":
        return 1
    else:
        return 0
    
def cpain(n):
    if n=="Typical Angina":
        return 1
    elif n=="Atypical Angina":
        return 2        
    elif n=="Non-anginal Pain":
        return 3
    elif n=="Asymptomatic":
        return 4
    
def HeartPred(lst):
    import requests

    # NOTE: you must manually set API_KEY below using information retrieved from your IBM Cloud account (https://dataplatform.cloud.ibm.com/docs/content/wsj/analyze-data/ml-authentication.html)
    API_KEY = "_kEjpRSJIqJ7sI2qiI8BUzJPXohJSaQD6cCED265Ur0m"
    token_response = requests.post('https://iam.cloud.ibm.com/identity/token', data={"apikey":
    API_KEY, "grant_type": 'urn:ibm:params:oauth:grant-type:apikey'})
    mltoken = token_response.json()["access_token"]

    header = {'Content-Type': 'application/json', 'Authorization': 'Bearer ' + mltoken}

    # NOTE: manually define and pass the array(s) of values to be scored in the next line
    payload_scoring = {"input_data": [{"field": [["age","sex","cp","trestbps","chol","fbs","restecg","thalach","exang","oldpeak","slope","ca","thal"]], "values": [lst]}]}

    response_scoring = requests.post('https://us-south.ml.cloud.ibm.com/ml/v4/deployments/170d3452-52ab-4846-8f26-f37b20f3f80e/predictions?version=2021-05-01', json=payload_scoring,
     headers={'Authorization': 'Bearer ' + mltoken})
    print("Scoring response")
    predictions = response_scoring.json()
    pred = predictions['predictions'][0]['values'][0][0]
    if (pred == 0):
        return "Less Chance of Heart Attack"
    else:
        return "More chance of Heart Attack"
        
        
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


st.markdown("<h1 style='text-align: center;'>Heart Attack Predictor</h1>",unsafe_allow_html=True)
with st.form("Form 1"):
    col1,col2,col4=st.columns(3)
    age=col1.number_input("Age",format="%.0f",min_value=28.0,max_value=80.0)
    sex=MF(col2.selectbox("Sex",options=("Male","Female")))
    trestbps=col4.number_input("Resting Blood Pressure",format="%.0f")
    cp=cpain(st.select_slider("Chest Pain Type :",options=("Typical Angina","Atypical Angina","Non-anginal Pain","Asymptomatic")))
    col5,col6,col7,col8=st.columns(4)
    chol=col5.number_input("Cholestral in mg/dl",format="%.0f")
    fbs=YN(col6.radio("Is Fasting Blood Sugar is > 120mg/dl",options=("Yes","No")))
    exang=YN(col7.radio("Exercise induced angina",options=("Yes","No")))   
    thalach=col8.number_input("Maximum heart rate achieved",format="%.0f")
    col9,col10,col11,col12,col13=st.columns(5)
    restecg=ecg(col9.selectbox("Resting ECG Results",options=("Normal","Having ST-T wave abnormality (T wave inversions and/or ST elevation or depression of > 0.05 mV)","Showing probable or definite left ventricular hypertrophy by Estes' criteria")))
    oldpeak=col10.number_input("Previous peak")
    slope=col11.number_input("Slope",format="%.0f")
    ca=col12.number_input("No. of major vessels",format="%.0f")
    thal=col13.number_input("Thal rate",format="%.0f")
    
    lst = [age,sex,cp,trestbps,chol,fbs,restecg,thalach,exang,oldpeak,slope,ca,thal]
    submit = st.form_submit_button('Predict')  
    
    if submit:
        progress_text = "Operation in progress. Please wait."
        my_bar = st.progress(0, text=progress_text)

        for percent_complete in range(100):
            time.sleep(0.6)
            my_bar.progress(percent_complete + 1, text=progress_text)
        time.sleep(1)
        my_bar.empty()
        st.text_area(label ="Model Prediction",value=HeartPred(lst), height =100)
    
