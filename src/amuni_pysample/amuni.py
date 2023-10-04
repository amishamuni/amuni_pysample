# Imports
import streamlit as st
import datetime

# Write to the streamlit app
st.title('My sample python repository')
st.write('Hey there!')

# Write to my console
now = datetime.datetime.now()
print ("Current date and time : ")
print (now.strftime("%Y-%m-%d %H:%M:%S"))

