def feedback():
    import streamlit as st
    st.markdown('* We will provide you water in next 6 hours.')
    st.markdown('* Please use the water according to use. Don\'t waste water')
    st.markdown('* If the water is not available we well contact you as soon as possible and guide you '
                'for that through the phone call provided by you')
    st.markdown('* For Contact:-\n'
                '1. Email: khushboo.21jice014@jietjodhpur.ac.in\n'
                '2. Contact number: 9983177800')


def feedback_tourist():
    import streamlit as st
    feedback()
    st.markdown('**Note**:- The water used by tourist is charged according to the usage amount explained on app info.')


def domestic_entries():
    import streamlit as st
    name = st.text_input('Enter Name *')
    address = st.text_input('Enter Address *')
    pincode = st.text_input('Enter Pincode *')
    aadhar = st.text_input('Enter Aadhar card number *')
    contact = st.text_input('Enter Contact number *')
    count = st.text_input('Enter Count of family members *')
    response = st.radio('Do you practice cattle culture', ('Yes', 'No'), index=1)
    c1 = c2 = c3 = c4 = c5 = '0'
    if response == 'Yes':
        st.write('Choose breeds you have *')
        op1 = st.checkbox('Cow')
        op2 = st.checkbox('Buffalo')
        op3 = st.checkbox('Sheep')
        op4 = st.checkbox('Dog')
        op5 = st.checkbox('Hen')

        st.write('Number of each breed *')
        c1 = st.text_input('Enter number of cows *')
        c2 = st.text_input('Enter number of buffaloes *')
        c3 = st.text_input('Enter number of sheep *')
        c4 = st.text_input('Enter number of dogs *')
        c5 = st.text_input('Enter number of hens *')

    return name, address, pincode, aadhar, contact, count, c1, c2, c3, c4, c5


def tourist_entries():
    import streamlit as st
    form, info = st.tabs(['Details', 'Info'])
    with form:
        name = st.text_input('Enter Hotel name *')
        address = st.text_input('Enter Address *')
        pincode = st.text_input('Enter Pincode *')
        uid = st.text_input('Enter Unique ID of hotel *')
        contact = st.text_input('Enter Contact number *')
        count = st.text_input('Enter Count of guest *')
        citizen = st.text_input('Enter Nationality *')
        checkin = st.time_input('Enter Check-in time *')
        checkout = st.time_input('Enter Check-out time *')
    with info:
        st.write('1. As per the guidelines, the water being used by the tourists per day is '
                 'at the rate of head charge of 8% of the total charge per day.')
        st.write('2. For Indian tourists the charges would be 8% of the total per head per day.')
        st.write('3. For VIP tourists the charges would be 15% of the total per head per day.')
        st.write('4. If there is lack of water in the main overhead tank of the city/district, '
                 'the charges may rise with 2% with previous. [For VIPs\' the addition will be of 4%.]')
        st.write('5. If water would be used mindfully by the tourist, while checking out 2% of the '
                 'total surplus charges would be returning to the payer/tourists [if not then at the end of '
                 'the month the amount will be transferred to the payer.]')
    return name, address, pincode, uid, contact, count, citizen, checkin, checkout


def agriculture_entries():
    import streamlit as st
    name = st.text_input('Enter Name *')
    address = st.text_input('Enter Address *')
    pincode = st.text_input('Enter Pincode *')
    contact = st.text_input('Enter Contact number *')
    area = st.text_input('Enter land area (sq. ft.)*')
    water_needed = st.text_input('Enter Water needed *')
    crope_type = st.text_input('Enter Crope type *')
    return name, address, pincode, contact, area, water_needed, crope_type
