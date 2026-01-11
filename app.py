import streamlit as st

st.title("Power Calculator")
st.write("Enter a number to calculate its power of 2, 3, 5.")

n = st.number_input("Enter a integer number ..", value = 1, step = 3)

sq = n ** 2
cube = n ** 3
fifth = n ** 5

st.write(f"square of  {n}  is :  {sq}")
st.write(f"cube of  {n}  is :  {cube}")
st.write(f"fifth power of  {n}  is :  {fifth}")