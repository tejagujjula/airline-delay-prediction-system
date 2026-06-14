import streamlit as st
import pandas as pd
import joblib
import plotly.express as px
import json

# ---------------------------
# Load Model & Columns
# ---------------------------
model = joblib.load("delay_rf_model.pkl")

# Load expected columns from JSON to avoid mismatch errors
with open("model_columns.json", "r") as f:
    expected_columns = json.load(f)

# ---------------------------
# Page Config
# ---------------------------
st.set_page_config(
    page_title="Airline Delay Prediction",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ---------------------------
# Theme Toggle
# ---------------------------
theme = st.sidebar.radio("🌗 Theme", ["Light", "Dark"])
if theme == "Dark":
    st.markdown(
        """
        <style>
        body { background-color: #121212; color: #f5f5f5; }
        .stSidebar, .css-1d391kg { background-color: #1e1e1e !important; }
        .stButton>button { background-color: #BB86FC; color: white; }
        h1, h2, h3, h4 { color: #BB86FC !important; }
        </style>
        """,
        unsafe_allow_html=True
    )
else:  # Light mode with contrast
    st.markdown(
        """
        <style>
        body { background-color: #ffffff; color: #1c1c1c; }
        .stSidebar, .css-1d391kg { background-color: #e9eef6 !important; }
        .stButton>button { background-color: #007BFF; color: white; }
        h1, h2, h3, h4 { color: #003366 !important; }
        label, .stMarkdown, .stTextInput>div>div>input, .stNumberInput>div>div>input {
            color: #000000 !important;
        }
        </style>
        """,
        unsafe_allow_html=True
    )

# ---------------------------
# Navigation
# ---------------------------
menu = st.sidebar.radio(
    "Navigation", ["Home", "Predict a Flight", "Visuals", "About", "Contact"]
)

# ---------------------------
# Home Section
# ---------------------------
if menu == "Home":
    st.title("✈️ Airline Delay Prediction & Management")
    st.markdown("""
    Flight delays cause **missed connections, higher costs, and unhappy passengers**.  
    This project uses **Machine Learning** to predict delay risks before departure, 
    so airlines can act early to improve efficiency.
    
    🔹 Reduces operational costs  
    🔹 Improves passenger satisfaction  
    🔹 Enables proactive scheduling  
    """)
    st.image("https://images.pexels.com/photos/912050/pexels-photo-912050.jpeg",
             use_container_width=True)

# ---------------------------
# Prediction Section
# ---------------------------
# ---------------------------
# Prediction Section
# ---------------------------
elif menu == "Predict a Flight":
    st.header("🔮 Predict Flight Delay")

    # Example list of IATA codes (expand as needed)
    airport_codes = ["ATL", "LAX", "ORD", "DFW", "JFK", "DEN", "SFO", "SEA", "LAS", "MIA"]

    col1, col2 = st.columns(2)

    with col1:
        origin = st.selectbox("Origin Airport Code", airport_codes)
        dest = st.selectbox("Destination Airport Code", airport_codes)
        dep_time = st.number_input("Scheduled Departure Time (HHMM)", 0, 2359, 1200)
        arr_time = st.number_input("Scheduled Arrival Time (HHMM)", 0, 2359, 1400)
        dep_delay = st.number_input("Departure Delay (mins)", -60, 600, 0)

    with col2:
        elapsed_time = st.number_input("Scheduled Elapsed Time (mins)", 10, 1000, 180)
        distance = st.number_input("Flight Distance (miles)", 50, 10000, 500)
        year = st.number_input("Year", 2019, 2025, 2023)
        month = st.slider("Month", 1, 12, 6)
        day_of_week = st.slider("Day of Week (1=Mon, 7=Sun)", 1, 7, 3)

    if st.button("Predict"):
        try:
            # Validation: Origin ≠ Destination
            if origin == dest:
                st.error("❌ Origin and Destination cannot be the same.")
            else:
                # Step 1: Build raw DataFrame
                raw_input = pd.DataFrame([[
                    origin, dest, dep_time, dep_delay, arr_time,
                    elapsed_time, distance, year, month, day_of_week
                ]], columns=expected_columns)

                # Step 2: Encode categorical variables
                input_encoded = pd.get_dummies(raw_input)

                # Step 3: Align with model columns
                import json
                model_columns = json.load(open("model_columns.json"))
                input_encoded = input_encoded.reindex(columns=model_columns, fill_value=0)

                # Step 4: Make prediction
                prediction = model.predict(input_encoded)[0]

                if prediction == 1:
                    st.error("⚠ Prediction: Flight is *Likely Delayed*")
                else:
                    st.success("✅ Prediction: Flight is *On-Time*")

        except Exception as e:
            st.error(f"Error in prediction: {e}")
# Visuals Section
# ---------------------------
elif menu == "Visuals":
    st.header("📊 Flight Delay Insights")

    # Example visuals (small size)
    sample_data = pd.DataFrame({
        "Status": ["On-Time", "Delayed"],
        "Count": [750, 250]
    })
    fig1 = px.pie(sample_data, names="Status", values="Count", title="Delay Distribution",
                  hole=0.4, width=400, height=400)
    st.plotly_chart(fig1, use_container_width=False)

    monthly = pd.DataFrame({
        "Month": list(range(1, 13)),
        "Delays": [120, 90, 140, 200, 180, 220, 300, 250, 230, 190, 160, 130]
    })
    fig2 = px.bar(monthly, x="Month", y="Delays", title="Delays per Month", width=500, height=400)
    st.plotly_chart(fig2, use_container_width=False)

# ---------------------------
# About Section
# ---------------------------
elif menu == "About":
    st.header("ℹ️ About this Project")
    st.markdown("""
    This project was developed during an **AI/ML Internship at Edubot Software and Services**.  
    It applies **Machine Learning models** such as Random Forest to predict airline delays.  
    
    ✅ Built with **Python, Scikit-learn, Pandas**  
    ✅ Dashboard created using **Streamlit + Plotly**  
    ✅ Helps improve **efficiency & passenger satisfaction**
    """)

# ---------------------------
# Contact Section
# ---------------------------
elif menu == "Contact":
    st.header("📬 Contact")
    st.write("For queries or collaboration, reach out:")
    st.markdown("""
    🔗 [LinkedIn](https://www.linkedin.com/in/teja-reddy-333a69291/)  
    💻 [GitHub](https://github.com/tejagujjula)  
    ✉️ Email: teja7102005@gmail.com
    """)
    st.success("Feel free to connect with me!")
