# ✈️ Airline Delay Prediction System

A Machine Learning web application that predicts whether a flight is likely to be delayed before departure. The system leverages historical flight data and operational parameters to identify potential delays, enabling proactive decision-making, improved operational efficiency, and enhanced passenger experience.

---

## 🚀 Features

* Flight delay prediction using **Random Forest Classifier**
* Interactive and user-friendly **Streamlit dashboard**
* Machine Learning-based delay prediction using historical flight data
* Input validation to prevent invalid or unrealistic predictions
* Delay insights and visualizations using **Plotly**
* Light and Dark theme support for enhanced user experience
* Real-time prediction results based on user-provided flight details

---

## 🛠️ Tech Stack

* **Language:** Python
* **Framework:** Streamlit
* **Libraries:** Scikit-learn, Pandas, NumPy, Plotly
* **Machine Learning Algorithm:** Random Forest Classifier
* **Model Serialization:** Pickle
* **Data Handling:** JSON

---

## 📊 Model Features

The model uses the following flight-related attributes for prediction:

| Feature                  | Description                                  |
| ------------------------ | -------------------------------------------- |
| Origin Airport           | Departure airport code                       |
| Destination Airport      | Arrival airport code                         |
| Scheduled Departure Time | Planned departure time                       |
| Departure Delay          | Historical/current departure delay (minutes) |
| Scheduled Arrival Time   | Planned arrival time                         |
| Scheduled Elapsed Time   | Total planned flight duration                |
| Flight Distance          | Distance between airports                    |
| Year                     | Year of travel                               |
| Month                    | Month of travel                              |
| Day of Week              | Day number (Monday = 1, Sunday = 7)          |

---

## 🧪 Run Locally

Follow these steps to run the project on your local machine:

```bash
# Clone the repository
git clone <repository-url>

# Navigate to the project directory
cd Airline-Delay-Prediction-System

# Install required dependencies
pip install -r requirements.txt

# Launch the Streamlit application
streamlit run app.py
```

---

## 📁 Project Structure

```text
Airline-Delay-Prediction-System/
│
├── app.py                           # Main Streamlit application
├── delay_rf_model.pkl               # Trained Random Forest model
├── model_columns.json               # Expected model input features
├── requirements.txt                 # Python dependencies
├── Dataset/
│   └── Flight_Delay_Cancellation_2019_2023_1.csv
└── README.md                        # Project documentation
```

---

## 📈 Dataset

The model was trained using historical flight data containing information related to flight schedules, delays, airport details, and operational parameters. The dataset was preprocessed and engineered to extract meaningful features for effective delay prediction.

---

## 📌 Notes

* The model predicts potential flight delays before departure using historical patterns and scheduling information.
* Ensure all required input fields are correctly filled to obtain accurate predictions.
* The application validates user inputs to prevent unrealistic flight scenarios (e.g., identical origin and destination airports).
* Prediction outcomes are intended to support operational planning and should not be considered definitive.

---

## 🔗 Links

* **GitHub Repository:** [GitHub Repository](https://github.com/your-username/airline-delay-prediction-system)
* **Live Demo:** [Streamlit Application](https://flight-delay-predictor-teja.streamlit.app)

---

## 👨‍💻 Developer

**Teja Reddy Gujjula**

* LinkedIn: https://www.linkedin.com/in/teja-reddy-g/
* GitHub: https://github.com/tejagujjula
* Email: [tejareddy_gujjula18@gmail.com](mailto:tejareddy_gujjula18@gmail.com)

---

### ⭐ If you found this project useful, consider giving it a star on GitHub!
