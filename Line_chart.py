import streamlit as st
import re
import matplotlib.pyplot as plt

collect_numbers = lambda x : [int(i) for i in re.split("[^0-9]", x) if i != ""]

numbers = st.text_input("PLease enter numbers")
if numbers :
    values = collect_numbers(numbers)

    fig, axis = plt.subplots(1)
    axis.plot(values)

    st.pyplot(fig=fig)