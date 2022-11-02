import streamlit as st

few_style="""
<style>
.e16nr0p34{
  height:50px;
  width:max-content;
  padding-left:20px;
  padding-right:20px;
  background-color:red;
}

</style>
"""


st.title("Predictive Maintainance")
st.subheader("By team Blizzard")

with st.form("myform1",clear_on_submit=True):
  voltage = st.text_input("Enter Voltage")
  rotation = st.text_input("Enter Rotation")
  Pressure = st.text_input("Enter Pressure")
  vibration = st.text_input("Enter Vibration")
  btn = st.form_submit_button("Submit")

  
if btn:
  st.markdown(few_style,unsafe_allow_html=True)
  st.write("Machine Fails")
