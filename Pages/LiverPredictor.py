import streamlit as st
import time

def LiverPred(lst):
    import requests

    # NOTE: you must manually set API_KEY below using information retrieved from your IBM Cloud account (https://dataplatform.cloud.ibm.com/docs/content/wsj/analyze-data/ml-authentication.html)
    API_KEY = "IKcgvqMhyL5y297xbSRKZeFkMOghaU5KFVHEF6qJQD5m"
    token_response = requests.post('https://iam.cloud.ibm.com/identity/token', data={"apikey":
    API_KEY, "grant_type": 'urn:ibm:params:oauth:grant-type:apikey'})
    mltoken = token_response.json()["access_token"]

    header = {'Content-Type': 'application/json', 'Authorization': 'Bearer ' + mltoken}

    # NOTE: manually define and pass the array(s) of values to be scored in the next line
    payload_scoring = {"input_data": [{"field": [["age","gender","tot_bilirubin","direct_bilirubin","tot_proteins","albumin","ag_ratio","sgpt","sgot","alkphos"]], "values": [lst]}]}

    response_scoring = requests.post('https://us-south.ml.cloud.ibm.com/ml/v4/deployments/72b69e55-1880-4b5a-ae15-584a65f67069/predictions?version=2021-05-01', json=payload_scoring,
     headers={'Authorization': 'Bearer ' + mltoken})
    print("Scoring response")
    predictions = response_scoring.json()
    pred = predictions['predictions'][0]['values'][0][0]
    if pred==1:
        return "You are NOT a liver patient"
    else:
        return "You are a liver patient"
        
        
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


st.markdown("<h1 style='text-align: center;'>Liver Disease Predictor</h1>",unsafe_allow_html=True)
with st.form("Form 1"):
    col1,col2,col3,col4=st.columns(4)
    age=col1.number_input("age",format= "%.0f",min_value=4.0,max_value=90.0,)
    gender=col2.selectbox("Gender",options=("Male","Female"))
    tot_bilirubin=col3.number_input("tot_bilirubin")
    direct_bilirubin=col4.number_input("direct_bilirubin")
    col5,col6,col7,col8=st.columns(4)
    tot_proteins=col5.number_input("tot_proteins", format="%.0f")
    albumin=col6.number_input("albumin", format="%.0f")
    ag_ratio=col7.number_input("ag_ratio", format="%.0f")
    sgpt=col8.number_input("sgpt")
    col9,col10=st.columns(2)
    sgot=col9.number_input("sgot")
    alkphos=col10.number_input("alkphos")
    lst = [age,gender,tot_bilirubin,direct_bilirubin,tot_proteins,albumin,ag_ratio,sgpt,sgot,alkphos]
    submit = st.form_submit_button('Predict')  
    
    if submit:
        progress_text = "Operation in progress. Please wait."
        my_bar = st.progress(0, text=progress_text)

        for percent_complete in range(100):
            time.sleep(0.6)
            my_bar.progress(percent_complete + 1, text=progress_text)
        time.sleep(1)
        my_bar.empty()
        st.text_area(label ="Model Prediction",value=LiverPred(lst), height =100)
    
