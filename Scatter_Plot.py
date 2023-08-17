import streamlit as st
import re
import matplotlib.pyplot as plt

collect_numbers = lambda x : [int(i) for i in re.split("[^0-9]", x) if i != ""]

x = st.text_input("PLease enter x values")
y = st.text_input("PLease enter y values")
if x and y :
    x = collect_numbers(x)
    y = collect_numbers(y)

    fig, axis = plt.subplots(1)
    axis.scatter(x,y)

    st.pyplot(fig=fig)