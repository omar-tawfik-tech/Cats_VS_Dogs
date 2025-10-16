import streamlit as st
import time
st.set_page_config(
    page_title="Dogs VS Cats",  # This changes the tab name
    page_icon="🐱",  # You can use multiple emojis
    layout='centered'
   
)
st.title("Dogs VS Cats")
st.header("There Is First End To End Deep Learning CNN Image Classification")
st.subheader("It Will Be A Binary Classification Detects IF It's A Cat Or Dog When You Enter The Image As An Input")
st.markdown("---")
json = {"Cat" :"0","Dog":"1"}
st.json(json)
st.sidebar.title("About My Self")
file = st.file_uploader("Upload a Photo", type=["Png", "Jpg"])




st.markdown("---")

with st.sidebar:
 Choosen_Platform = st.selectbox("Choose The Platform: ", ["LinkedIn","Github",'Kaggle'])

if Choosen_Platform == "Kaggle":
   st.markdown('[Kaggle](https://www.kaggle.com/omarsayedtawfik)')
     

if Choosen_Platform == "LinkedIn":
   st.markdown('[LinkedIn](https://www.linkedin.com/in/omar-sayed-b68602243/)')
    
if Choosen_Platform == "Github":
   st.markdown('[Github](https://github.com/omar-tawfik-tech)')
    


     
     