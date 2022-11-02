import streamlit as st
from pycaret.classification import *
import pandas


st.title("Predictive Maintainance")
st.subheader("By team Blizzard")

data = st.file_uploader("Upload input CSV file",type=["csv"])
st.dataframe(data)
# if st.button("Predict"):
  


def forcast(data):
    saved_final_lr = load_model('Final_LR_Model')
    new_prediction = predict_model(saved_final_lr, data=data)
    return new_prediction


