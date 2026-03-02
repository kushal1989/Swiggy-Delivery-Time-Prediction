import streamlit as st
import pandas as pd
import pickle

st.title("Swiggy Delivery Time Prediction")
st.write("Enter order details to predict delivery time (in minutes)")

with open("model.pkl", "rb") as file:
    model = pickle.load(file)

with open("final_features.pkl", "rb") as file:
    final_features = pickle.load(file)

with open("scaler.pkl", "rb") as file:
    scaler = pickle.load(file)


# ================= INPUTS =================

age = st.number_input("Rider Age", min_value=18, max_value=60)

ratings = st.slider("Rider Ratings", 1.0, 5.0, step=0.1)

vehicle_condition = st.selectbox(
    "Vehicle Condition",
    [0, 1, 2],
    format_func=lambda x: ["Poor", "Average", "Good"][x]
)

multiple_deliveries = st.number_input(
    "Multiple Deliveries Assigned", min_value=0, max_value=5
)

distance = st.number_input("Distance (km)", min_value=0.1)

traffic = st.selectbox(
    "Traffic Level",
    [0, 1, 2],
    format_func=lambda x: ["Low", "Medium", "High"][x]
)

order_time_hour = st.slider("Order Time (Hour)", 0, 23)

festival_yes = st.selectbox("Festival Day?", ["No", "Yes"])

order_time_of_day_morning = st.selectbox(
    "Order Time of Day",
    ["Morning", "Other"]
)

weather_sunny = st.selectbox("Weather", ["Sunny", "Other"])

city_type_urban = st.selectbox("City Type", ["Urban", "Semi-Urban"])


# ================= DATAFRAME =================

input_data = pd.DataFrame({
    "age": [age],
    "ratings": [ratings],
    "vehicle_condition": [vehicle_condition],
    "multiple_deliveries": [multiple_deliveries],
    "distance": [distance],
    "traffic": [traffic],
    "order_time_hour": [order_time_hour],
    "festival_yes": [1 if festival_yes == "Yes" else 0],
    "order_time_of_day_morning": [1 if order_time_of_day_morning == "Morning" else 0],
    "weather_sunny": [1 if weather_sunny == "Sunny" else 0],
    "city_type_urban": [1 if city_type_urban == "Urban" else 0]
})

input_data = input_data[final_features]


# ================= SCALING =================

input_scaled = scaler.transform(input_data)


# ================= PREDICTION =================

if st.button("Predict Delivery Time"):
    prediction = model.predict(input_scaled)[0]
    st.success(f"Estimated Delivery Time: **{prediction:.2f} minutes**")
