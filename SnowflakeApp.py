import streamlit as st

few_style="""
<style>
.e16nr0p34 p{
  height:max-content;
  width:max-content;
  padding:20px;
  color:white;
  background-color:red;
}

</style>
"""


st.title("Predictive Maintainance")
st.subheader("By team Blizzard")
temp = False
with st.form("myform1",clear_on_submit=True):
  voltage = st.text_input("Enter Voltage",on_change=onChangeFunc)
  rotation = st.text_input("Enter Rotation",on_change=onChangeFunc)
  Pressure = st.text_input("Enter Pressure",on_change=onChangeFunc)
  vibration = st.text_input("Enter Vibration",on_change=onChangeFunc)
  btn = st.form_submit_button("Submit")

  
if btn:
  temp = True

if temp:
  st.markdown(few_style,unsafe_allow_html=True)
  st.write("Machine Fails")
  
def onChangeFunc():
  temp = False
