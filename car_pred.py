import pandas as pd
import streamlit as st
import pickle
import sklearn as sk


st.header('Cars 24 Price Prediction App')
df = pd.read_csv("cars24-car-price.csv")
# we dont see dataframe in general
# st.dataframe(df)

fuel_type = st.selectbox(
    "Select Fuel Type:",
    ("Petrol", "Diesel", "CNG", "Electric", "LPG")
)

# slider
engine = st.slider("Set the Engine Power", 500, 5000, step =100)

col1, col2 = st.columns(2)

with col1:
    transmission_type = st.selectbox(
        "Select Transmission Type", ("Manual", "Automatic")
    )

with col2:
    seats = st.selectbox(
        "Select number of seats ", [4, 5, 6, 7, 8]
    )

# now encode dict fuel type and transmission type
encode_dict = {
    "fuel_type": {"Diesel": 1, "Petrol": 2, "CNG": 3, "LPG": 4, "Electric": 5},
    "transmission_type": {"Manual": 1, "Automatic": 2}
}

# we are not making model we are just loading it
def model_pred(fuel_encoded, transmission_encoded, seats, engine):
    with open("car_pred", "rb") as file:
        reg_model = pickle.load(file)
        #bring all input featues ideally we should take all values from users but for
        #time limitation we are taking few values from users and other giving as default values ourseleves
        input_features = [[2018.0, 1, 120000, fuel_encoded, transmission_encoded, 19.7, engine, 46.3, seats]]
        return reg_model.predict(input_features)

# if button presses then 1st we encode then calculate
# [fuel_type] represent = input from web, lets say Diesel
# encode_dict['fuel_type'] encoded the fuel_type 1
if st.button("Predict"):
    fuel_encoded = encode_dict['fuel_type'][fuel_type]
    transmission_encoded = encode_dict['transmission_type'][transmission_type]
    # Call my model
    price = model_pred(fuel_encoded, transmission_encoded, seats, engine)
    #warning disregard
    st.text("Predicted Price is " + str(price))


