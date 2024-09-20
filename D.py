import streamlit as st
#functions
col3=st.columns(1)
data=0
   


def name():
    st.header("SRM PYTHON SEMINAR")
    name = st.text_input("Enter a name")
    num1 = st.text_input("Enter a number1:")
    num2 = st.text_input("Enter a number2:")
    with col3:
        st.header(name)  
        if st.button("add"):
            st.title(int(num1)+int(num2))
        if st.button("sub"):
            st.title(int(num1)-int(num2))
        if st.button("mul"):
            st.title(int(num1)*int(num2))
        if st.button("div"):
            st.title(int(num1)/int(num2))

def ar():
    st.header ("Result")
    nu1 = st.number_input("Enter a number1:")
    nu2 = st.number_input("Enter a number2:")
    if st.button ("area"):  
       data = int(nu1)*int(nu2)
       st.title(data)
def year():
    no_of_days = st.number_input("Enter number:")
    years = int(no_of_days) //365
    months = (int(no_of_days) % 365) //30
    days = (int(no_of_days) % 365) %30
    st.text(f"Years:{years}, Months: {months}, days: {days}")


def temp():
    t=st.number_input("Temperature:") 
    if st.button("Check"):
        if t>1000:
            st.error("High")
        elif 500<t<1000:
            st.warning("Medium")
        elif t<500:
            st.success("Low")
temp()
        
