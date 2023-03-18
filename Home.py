import streamlit as st
from Backend import *
from csv import DictWriter
import os
from google.cloud import firestore

# Authenticate to Firestore with the JSON account key.
db = firestore.Client.from_service_account_json("we-love-water-firebase-adminsdk-82y8k-3fd7edd8e6.json")

# Create a reference to the Google post.
domestic = db.collection("domestic_record").document("606lcU5ENeODhm4dXo3q")

tourist = db.collection("tourist_record").document("B7TCrXyCFalM0tePcCNZ")

agriculture = db.collection("agriculture_record").document("9J5dRc5hWLf8V97lY83S")

# adding page name
st.set_page_config(page_title='We Love Water', page_icon='💧')

# adding logo image
st.image('logo.jpeg')

# adding title
st.header('We Love Water')

# adding radio button
use_type = st.radio('Select your usage type', ('Domestic', 'Tourist', 'Agriculture'))

# creating container
contain = st.empty()

# declaring fields
name = address = pincode = aadhar = contact = count = uid = citizen = checkin = checkout = \
    area = water_needed = crope_type = None
c1 = c2 = c3 = c4 = c5 = ''

# adding choose condition
if use_type == 'Domestic':
    with contain.container():
        name, address, pincode, aadhar, contact, count, c1, c2, c3, c4, c5 = domestic_entries()

elif use_type == 'Tourist':
    with contain.container():
        name, address, pincode, uid, contact, count, citizen, checkin, checkout = tourist_entries()
else:
    with contain.container():
        name, address, pincode, contact, area, water_needed, crope_type = agriculture_entries()

back = st.empty()
submit = st.empty()

# adding submit button
with submit.container():
    submit_button = st.button('Submit')

# adding back button
with back.container():
    if st.button('Back'):
        contain.empty()
        back.empty()
        submit.empty()

# checking for submit condition
if submit_button:
    # save data for domestic
    if use_type == 'Domestic':
        domestic.set({
                'Name': name,
                'Address': address,
                'Pincode': pincode,
                'Aadhar No.': aadhar,
                'Contact No': contact,
                'Family size': count,
                'Animal name': ['Cow', 'Buffalo', 'Dog', 'Sheep', 'Hen'],
                'Animal Count': [c1, c2, c3, c4, c5],
                'Water Required': 20 * int(count) + 80 * int(c1) + 100 * int(c2)
                                  + 10 * int(c3) + 2 * int(c4) + 5 * int(c5)
            })

    # save data for tourist
    elif use_type == 'Tourist':
        tourist.set({
                'Name': name,
                'Address': address,
                'Pincode': pincode,
                'Unique ID': uid,
                'Contact No': contact,
                'No of Guests': count,
                'Nationality': citizen,
                'Check-in': checkin,
                'Check-out': checkout,
                'Water Required': 18 * int(count)
            })

    # save data for agriculture
    else:
        agriculture.set({
                'Name': name,
                'Address': address,
                'Pincode': pincode,
                'Contact No': contact,
                'Land Area': area,
                'Crope Type': crope_type,
                'Water Required': water_needed
            })

    contain.empty()
    if use_type == 'Tourist':
        feedback_tourist()
    else:
        feedback()
    back.empty()
    submit.empty()
