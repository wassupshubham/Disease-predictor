import streamlit as st
import time

def YN(n):
    if n=="Yes":
        return 1
    else:
        return 0

def MigranePred(lst):
    import requests

    # NOTE: you must manually set API_KEY below using information retrieved from your IBM Cloud account (https://dataplatform.cloud.ibm.com/docs/content/wsj/analyze-data/ml-authentication.html)
    API_KEY = "xZTXObrkExtxVd0PT-NDspCGkVqXP1grM1KP6W84qSFv"
    token_response = requests.post('https://iam.cloud.ibm.com/identity/token', data={"apikey":
    API_KEY, "grant_type": 'urn:ibm:params:oauth:grant-type:apikey'})
    mltoken = token_response.json()["access_token"]

    header = {'Content-Type': 'application/json', 'Authorization': 'Bearer ' + mltoken}

    # NOTE: manually define and pass the array(s) of values to be scored in the next line
    payload_scoring = {"input_data": [{"field": [["Age","Duration","Frequency","Location","Character","Intensity""Nausea","Vomit","Phonophobia","Photophobia","Visual","Sensory","Dysphasia","Dysarthria","Vertigo","Tinnitus","Hypoacusis","Diplopia","Defect","Ataxia","Conscience","Paresthesia","DPF"]], "values": [lst]}]}

    response_scoring = requests.post('https://us-south.ml.cloud.ibm.com/ml/v4/deployments/md/predictions?version=2021-05-01', json=payload_scoring,
     headers={'Authorization': 'Bearer ' + mltoken})
    print("Scoring response")
    predictions = response_scoring.json()
    pred = predictions['predictions'][0]['values'][0][0]
    return pred
        
        
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

st.markdown("<h1 style='text-align: center;'>Migrane Predictor</h1>",unsafe_allow_html=True)
with st.form("Form 1"):
    col1,col2,col3,col4=st.columns(4)
    Age=col1.number_input("Age", format="%.0f", min_value=15.0,max_value=80.0)
    Duration=col2.number_input("Duration", format="%.0f")
    Frequency=col3.number_input("Frequency", format="%.0f")
    Location=col4.number_input("Location", format="%.0f")
    col5,col6,col7,col8=st.columns(4)
    Character=col5.number_input("Character", format="%.0f")
    Intensity=col6.slider("Intensity", 0, 3)
    
    Visual=col7.number_input("Visual", format="%.0f")
    Sensory=col8.number_input("Sensory", format="%.0f")
    
    
    col9,col10,col11,col12=st.columns(4)
    Nausea=YN(col11.radio("Nausea",options=("Yes","No")))

    Vomit=YN(col12.radio("Vomit",options=("Yes","No")))
    Phonophobia=YN(col9.radio("Phonophobia",options=("Yes","No")))
    Photophobia=YN(col10.radio("Photophobia",options=("Yes","No")))
    
    col13,col14,col15,col16=st.columns(4)
    Dysphasia=YN(col13.radio("Dysphasia",options=("Yes","No")))

    Dysarthria=YN(col14.radio("Dysarthria",options=("Yes","No")))

    Vertigo=YN(col15.radio("Vertigo",options=("Yes","No")))

    Tinnitus=YN(col16.radio("Tinnitus",options=("Yes","No")))

    col17,col18,col19,col20=st.columns(4)
    Hypoacusis=YN(col17.radio("Hypoacusis",options=("Yes","No")))
    Diplopia=YN(col18.radio("Diplopia",options=("Yes","No")))
    Defect=YN(col19.radio("Defect",options=("Yes","No")))
    Ataxia=YN(col20.radio("Ataxia",options=("Yes","No")))
    col21,col22,col23=st.columns(3)
    Conscience=YN(col21.radio("Conscience",options=("Yes","No")))
    Paresthesia=YN(col22.radio("Parenthesia",options=("Yes","No")))
    DPF=YN(col23.radio("DPF",options=("Yes","No")))
    lst = [Age,Duration,Frequency,Location,Character,Intensity,Nausea,Vomit,Phonophobia,Photophobia,Visual,Sensory,Dysphasia,Dysarthria,Vertigo,Tinnitus,Hypoacusis,Diplopia,Defect,Ataxia,Conscience,Paresthesia,DPF]
    submit = st.form_submit_button('Predict') 
    
    if submit:
        progress_text = "Operation in progress. Please wait."
        my_bar = st.progress(0, text=progress_text)

        for percent_complete in range(100):
            time.sleep(0.6)
            my_bar.progress(percent_complete + 1, text=progress_text)
        time.sleep(1)
        my_bar.empty()
        st.text_area(label ="Model Prediction",value=MigranePred(lst), height =100)
    
