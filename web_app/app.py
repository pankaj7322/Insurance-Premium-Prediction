import streamlit as st
import pickle
import numpy as np
import os

# Get the path to the data file
base_dir = os.path.dirname(__file__)
file_path = os.path.join(base_dir,'model.pkl')


# import the model
with open(file_path, 'rb') as file:
    model = pickle.load(file)


# Define custom HTML for styling the header
header_html = """
    <style>
        .header-box {
            background-color: orange;  /* Background color */
            color: white;               /* Text color */
            padding: 10px;                /* Padding inside the box */
            border-radius: 5px;         /* Rounded corners */
            text-align: center;         /* Center text alignment */
            font-size: 16px;            /* Font size */
        }
    </style>
    <div class="header-box">
        <h1>Insurance Premium Prediction</h1><br>
    </div>
"""

# Render the custom HTML in Streamlit
st.markdown(header_html, unsafe_allow_html=True)

st.subheader("Prediction")

# Create a form
st.sidebar.subheader("Please Enter the value")

# Input fields
def input_fields():
    age = st.sidebar.slider('Select Age: ', min_value=18, max_value = 64, value=18)

    # for gender
    gender_mapping = {
        "Female":0,
        "Male": 1
    }
    # created the select box with labels
    gender_labels = st.sidebar.selectbox("Select Gender", options=list(gender_mapping.keys()))
    # Convert the selected label to its corresponding value
    gender_value = gender_mapping[gender_labels]

    bmi = st.sidebar.text_input("Enter BMI:")
    children = st.sidebar.text_input("Enter number of children")

    # for smoker
    smoker_mapping = {
        "No" : 0,
        "Yes" : 1
    }

    #created the radio box with lables
    smoker_labels = st.sidebar.radio("Smoker Choose one",list(smoker_mapping.keys()))

    # convert the selected label to its correspoinding value
    smoker_value = smoker_mapping[smoker_labels]


    # for region
    region_mapping = {
        "Northeast" : 0,
        "Northwest" : 1,
        "Southeast" : 2,
        "Southwest" : 3,
    }
    # created the select box with labels
    region_labels = st.sidebar.selectbox("Select Region", options = list(region_mapping.keys()))

    # convert the selected label to its corresponding value
    region_value = region_mapping[region_labels]
    submit = st.sidebar.button("Submit")

    if submit:
        if not bmi:
            st.error("❌ BMI cannot be empty.")
        elif not children:
            st.error("❌ Children cannot be empty.")
        else:
            predict = model.predict([[age,gender_value,bmi,children,smoker_value,region_value]])

            #text area of output prediction
         
            st.markdown(f"""
                <div style="border: none;
                 padding: 10px; border-radius: 5px; 
                 background-color: lightgreen;
                 color:black">
                    {predict[0]}.
                    </div>
                """, unsafe_allow_html=True)



if __name__ == '__main__':
    input_fields()
