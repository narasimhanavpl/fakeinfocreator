from faker import Faker
import streamlit as st

fake = Faker('en_IN')


age = st.slider('Minimum and Maximum age', age_min, age_max, (25,50))

def create():
    st.write('Name: ' + fake.name())
    st.write('Address: ' + fake.address())
    st.write('City of birth: ' + fake.city())
    st.write('Date of Birth: ' + str(fake.date_of_birth(minimum_age = int(age_min), maximum_age = int(age_max))))
    st.write('Occupation: ' + fake.job())

create()


