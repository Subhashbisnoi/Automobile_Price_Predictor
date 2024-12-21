import streamlit as st
import pickle
import pandas as pd

# Load the trained models
with open("LinearRegressionModel_Car.pkl", "rb") as car_file:
    car_model = pickle.load(car_file)

with open("LinearRegressionModel_Bike.pkl", "rb") as bike_file:
    bike_model = pickle.load(bike_file)

# Load the datasets
cars_df = pd.read_csv("Cleaned_car.csv")
bikes_df = pd.read_csv("Cleaned_bike.csv")

# Sidebar: Select Vehicle Type
st.sidebar.header("Automobile Price Prediction")
vehicle_type = st.sidebar.radio("Select Vehicle Type", ["Car", "Bike"])

if vehicle_type == "Car":
    # Step 1: Select company
    company = st.sidebar.selectbox("Select Car Company", cars_df["company"].unique())

    # Step 2: Filter car names based on selected company
    filtered_names = cars_df[cars_df["company"] == company]["name"].unique()
    name = st.sidebar.selectbox("Select Car Name", filtered_names)

    # Step 3: Other inputs
    fuel_type = st.sidebar.selectbox("Fuel Type", ["Petrol", "Diesel"])
    year = st.sidebar.slider("Year of Manufacture", 2000, 2023, 2015)
    kms_driven = st.sidebar.number_input("Kilometers Driven", min_value=0, max_value=500000, step=1000)

    # Prepare the input data
    if year < 2009:
        st.sidebar.error("You cannot buy/sell cars older than 15 years!")
    else:
        input_data = pd.DataFrame({
            "name": [name],
            "company": [company],
            "fuel_type": [fuel_type],
            "year": [year],
            "kms_driven": [kms_driven]
        })

        # Prediction
        if st.sidebar.button("Predict Price"):
            try:
                predicted_price = car_model.predict(input_data)[0]
                if predicted_price < 20000:
                    predicted_price = 19050
                st.write(f"### Predicted Car Price: ₹{predicted_price:,.2f}")
            except Exception as e:
                st.write("Error in prediction:", e)

elif vehicle_type == "Bike":
    # Step 1: Select bike name
    bike_name = st.sidebar.selectbox("Select Bike Name", bikes_df["name"].unique())

    # Step 2: Other inputs
    year = st.sidebar.slider("Year of Manufacture", 2000, 2023, 2015)
    kms_driven = st.sidebar.number_input("Kilometers Driven", min_value=0, max_value=500000, step=1000)

    # Prepare the input data
    if year < 2009:
        st.sidebar.error("You cannot buy/sell bikes older than 15 years!")
    else:
        input_data = pd.DataFrame({
            "name": [bike_name],
            "year": [year],
            "km_driven": [kms_driven]
        })

        # Prediction
        if st.sidebar.button("Predict Price"):
            try:
                predicted_price = bike_model.predict(input_data)[0]
                if predicted_price < 10000:
                    predicted_price = 9500
                st.write(f"### Predicted Bike Price: ₹{predicted_price:,.2f}")
            except Exception as e:
                st.write("Error in prediction:", e)

# Display instructions
st.write("### Instructions")
st.write("""
1. Choose whether you want to predict the price of a car or a bike.
2. For cars:
    - Select the car company and car name.
    - Provide the year of manufacture, kilometers driven, and fuel type.
3. For bikes:
    - Select the bike name.
    - Provide the year of manufacture and kilometers driven.
4. Click on the 'Predict Price' button to see the predicted price.
""")