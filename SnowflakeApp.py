import streamlit as st

few_style="""
<style>
[data-test-id="stMarkdownContainer"]{
  height:50px;
  width:50px;
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
  st.write("Machine Fails")
