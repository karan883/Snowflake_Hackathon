import streamlit as st
st.title("Predictive Maintainance")
st.subheader("By team Blizzard")

with st.form():
  voltage = st.text_input("Enter Voltage")
  rotation = st.text_input("Enter Rotation")
  Pressure = st.text_input("Enter Pressure")
  vibration = st.text_input("Enter Vibration")
