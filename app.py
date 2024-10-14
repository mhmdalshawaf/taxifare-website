import streamlit as st
import requests

# Title of the application
st.title("Taxi Fare Prediction")

# Description
st.markdown('''
## Please provide the following parameters to get a fare estimate for your ride:
''')

# Input fields for user parameters
date_time = st.date_input("Date and Time", value=None)
pickup_longitude = st.number_input("Pickup Longitude", format="%.6f", help="Enter the longitude of your pickup location.")
pickup_latitude = st.number_input("Pickup Latitude", format="%.6f", help="Enter the latitude of your pickup location.")
dropoff_longitude = st.number_input("Dropoff Longitude", format="%.6f", help="Enter the longitude of your dropoff location.")
dropoff_latitude = st.number_input("Dropoff Latitude", format="%.6f", help="Enter the latitude of your dropoff location.")
passenger_count = st.number_input("Passenger Count", min_value=1, max_value=6, value=1, help="Select the number of passengers.")

# Prediction API URL
url = 'https://taxifare2-292885400961.europe-west1.run.app/predict'

# Button to submit the request
if st.button("Get Prediction"):
    # Prepare the request payload
    payload = {
        "pickup_datetime": date_time.isoformat(),
        "pickup_longitude": pickup_longitude,
        "pickup_latitude": pickup_latitude,
        "dropoff_longitude": dropoff_longitude,
        "dropoff_latitude": dropoff_latitude,
        "passenger_count": passenger_count
    }

    # Call the API
    try:
        response = requests.post(url, json=payload)
        response.raise_for_status()  # Raise an error for bad responses
        result = response.json()

        # Displaying the result
        fare_estimate = result.get("fare", "No fare estimate available.")
        st.success(f"The estimated fare is: ${fare_estimate:.2f}")
    except requests.exceptions.RequestException as e:
        st.error(f"Error: {e}")

# Additional information
st.markdown('''
### Note:
You can use your own API for the prediction or the one provided by Le Wagon.
''')
