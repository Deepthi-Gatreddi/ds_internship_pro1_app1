import streamlit as st

st.title("Innomatics Data App :- Assigment 1")
btn_click = st.button("Click Me!")

if btn_click == True:
    st.subheader("You clicked me :smirk:")
    st.write("This Page Contains Information about the Fruits")
    st.snow()