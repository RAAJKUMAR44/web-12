import streamlit as st 
import pandas as pd 

# title
st.title("Welcome to My Website")
st.header("Python Streamlit Framework")
st.subheader("JAVA language is my next target")
st.markdown("I Love Her once upon a time!")
st.markdown("Inshallah i will showcase my project in CSE fest!")
st.markdown("I want to be highlighted in CSE fest!!")

st.code("""for i in range(1,5,1):
                print("Hello Developer!")
                """)

# extract excel sheet
dataset = pd.read_excel("Top 20.xlsx")
st.dataframe(dataset)

# create form
name = st.text_input("Enter Your Name: ")
fname = st.text_input("Enter Your Father Name: ")
adr = st.text_area("Enter Your Address: ")
classdata = st.selectbox("Enter Your Class: ", (1, 2, 3, 4, 5))

# create button
button = st.button("Done")
if button:
    st.markdown(f"""
    Name : {name}\n
    Father Name : {fname}\n
    Address : {adr}\n
    Class : {classdata}
    """)
