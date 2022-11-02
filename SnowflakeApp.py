import streamlit as st
from pycaret.classification import *
import pandas


st.title("Predictive Maintainance")
st.subheader("By team Blizzard")

udata = st.file_uploader("Upload input CSV file",type=["csv"])
if udata is not None:
    udata = pd.read_csv(udata)
submit = st.button('Predict')

def forcast(data):
    saved_final_lr = load_model('Final_LR_Model')
    new_prediction = predict_model(saved_final_lr, data=data)
    return new_prediction

if submit:
    result = forcast(udata)
    st.dataframe(result)
    csv_result = result.to_csv(index=False).encode('utf-8')
    st.download_button("Download Results",csv_result,"result.csv","text/csv",key='download-csv')
