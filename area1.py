import streamlit as st
import pickle

# Load model
model1 = pickle.load(open("area.pk1", "rb"))

def myf1():
    st.title("House Price Predictor")

    area = st.number_input("Enter the area value:")

    if st.button("Predict"):
        op = model1.predict([[area]])
        st.write("Price of the area is: ₹", round(op[0], 2))

myf1()
