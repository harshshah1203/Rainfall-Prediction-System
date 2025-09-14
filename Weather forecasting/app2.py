import streamlit as st
import pandas as pd

# --- PAGE CONFIGURATION ---
st.set_page_config(
    page_title="Rainfall Prediction Forecaster",
    page_icon="☔",
    layout="wide"
)

# --- SIMULATED PREDICTION FUNCTION ---
# This function mimics your trained model's behavior based on the new features.
def make_prediction(pressure, dewpoint, humidity, cloud, sunshine, winddirection, windspeed):
    """
    Simulates a rainfall prediction based on the features from the notebook.
    Returns:
        - Predicted Weather (str)
        - Probability of Rain (str)
        - URL for a relevant image (str)
    """
    # Image URLs from a placeholder service.
    image_urls = {
        "Rainy": "https://placehold.co/600x350/7C96AB/FFFFFF?text=Rainy+Weather",
        "Cloudy": "https://placehold.co/600x350/B0C4DE/FFFFFF?text=Cloudy+Weather",
        "Sunny": "https://placehold.co/600x350/FFD700/000000?text=Sunny+Weather"
    }

    # Rule-based logic simulating the model's decision process.
    if pressure < 1010 and humidity > 80 and cloud > 75 and sunshine < 2:
        return "Heavy Rain Expected", "88% Chance of Rain", image_urls["Rainy"]
            
    elif pressure < 1015 and humidity > 70 and cloud > 60 and windspeed > 20:
        return "Light Showers Possible", "60% Chance of Rain", image_urls["Cloudy"]

    elif pressure > 1020 and sunshine > 8 and cloud < 25:
        return "No Rain Expected", "15% Chance of Rain", image_urls["Sunny"]
            
    else:
        return "Partly Cloudy, Unlikely Rain", "30% Chance of Rain", image_urls["Cloudy"]

# --- SIDEBAR FOR MANUAL INPUT ---
st.sidebar.header("Manual Weather Input")
st.sidebar.markdown("Enter the conditions to get a rainfall prediction.")

# Input widgets based on the notebook's features
pressure_input = st.sidebar.slider("💨 Pressure (hPa)", 990, 1040, 1015)
dewpoint_input = st.sidebar.slider("🌡️ Dew Point (°C)", -5, 30, 19)
humidity_input = st.sidebar.slider("💧 Humidity (%)", 10, 100, 85)
cloud_input = st.sidebar.slider("☁️ Cloud Cover (%)", 0, 100, 81)
sunshine_input = st.sidebar.slider("☀️ Sunshine (hours)", 0.0, 13.0, 0.5)
winddir_input = st.sidebar.slider("🧭 Wind Direction (°)", 0, 360, 40)
windspeed_input = st.sidebar.slider("🌬️ Wind Speed (km/h)", 0, 60, 14)

predict_button = st.sidebar.button("Predict Rainfall", use_container_width=True)


# --- MAIN PAGE ---
st.title("☔ Rainfall Prediction Forecaster")
st.markdown("Get an instant rainfall forecast based on current weather data.")

# --- PREDICTION DISPLAY ---
if predict_button:
    weather, probability, image_url = make_prediction(
        pressure_input, 
        dewpoint_input, 
        humidity_input, 
        cloud_input, 
        sunshine_input, 
        winddir_input, 
        windspeed_input
    )

    st.header("Prediction Results")
    col1, col2 = st.columns([1, 2])

    with col1:
        st.subheader("Input Data")
        st.metric(label="Pressure", value=f"{pressure_input} hPa")
        st.metric(label="Dew Point", value=f"{dewpoint_input} °C")
        st.metric(label="Humidity", value=f"{humidity_input} %")
        st.metric(label="Cloud Cover", value=f"{cloud_input} %")
        st.metric(label="Sunshine", value=f"{sunshine_input} hrs")
        st.metric(label="Wind Direction", value=f"{winddir_input}°")
        st.metric(label="Wind Speed", value=f"{windspeed_input} km/h")

    with col2:
        st.subheader("Forecast")
        st.image(image_url, caption=f"Predicted Weather: {weather}")
        st.success(f"**Forecast: {weather}**")
        st.info(f"**Probability: {probability}**")
else:
    st.info("Enter data in the sidebar and click 'Predict Rainfall' to see the forecast here.")


# --- SPACER & FILE UPLOADER ---
st.markdown("---")
st.header("Or, Upload and View Historical Weather Data")
uploaded_file = st.file_uploader("Choose a CSV file", type="csv")

if uploaded_file is not None:
    try:
        df = pd.read_csv(uploaded_file)
        st.subheader("Data Preview from your CSV file")
        st.dataframe(df)
    except Exception as e:
        st.error(f"Error reading file: {e}")

