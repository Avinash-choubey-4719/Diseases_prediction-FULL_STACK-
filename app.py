import streamlit as st
import json
from streamlit_lottie import st_lottie



def Compare(selected_company_name_1,selected_company_name_2):
     col1,col2=st.columns(2)
     with col1:
         st.header(selected_company_name_1)
         st.subheader('Accuracy : ')
         st.subheader("96.66 %")

     with col2:
        st.header(selected_company_name_2)
        st.subheader('Accuracy : ')
        st.subheader("91.55%")


st. set_page_config(page_title="Diases Prediction",layout="wide")       
st.sidebar.title('Compare Model')
selected_company_name_1 = st.sidebar.selectbox(
    'Select By Model Name',
   [ 'Naive Bayes','Decision Tree'])

st.sidebar.write('You selected:', selected_company_name_1)
selected_company_name_2 = st.sidebar.selectbox(
    'Select By Model Name',
     [ 'Naive Bayes','Decision Tree'],key=1)
st.sidebar.write('You selected:', selected_company_name_2)
if st.sidebar.button('Compare'):
     Compare(selected_company_name_1,selected_company_name_2)
