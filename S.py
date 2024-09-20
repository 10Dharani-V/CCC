import streamlit as st
class buttons:
    def __init__(self, button_name):
        if st.button(f"Button Number is {button_name}"):
            self.calc(int(button_name)**2)
    def calc(self,button_name):
        if button_name % 2==0:
            st.balloons()
        else:
            st.snow()
def num():
    for i in range(5):
        buttons(i)
num()
def string():
    a= "Hello Python Program"
    st.title(a)
    st.title(a[0])
    st.title(a[0:4])
    st.title(a[1:9:2])
string()