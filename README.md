# Automobile Price Predictor

This is a Streamlit-based web application that predicts the prices of cars and bikes. Users can select either cars or bikes, input relevant details such as company, model, year of manufacture, kilometers driven, and fuel type (for cars), and get an estimated price using a trained machine learning model.

## Features

- **Car Price Prediction:** Predicts the price of cars based on attributes like company, model, fuel type, manufacturing year, and kilometers driven.
- **Bike Price Prediction:** Predicts the price of bikes based on attributes like model, manufacturing year, and kilometers driven.
- **User-Friendly Interface:** Intuitive UI built with Streamlit for seamless user experience.
- **Model Training:** Models trained using Linear Regression for accuracy in predictions.

## How It Works

1. Select whether you want to predict the price of a car or a bike.
2. For cars:
   - Select the car company.
   - Select the car model from the list.
   - Choose fuel type.
   - Enter the year of manufacture.
   - Enter the kilometers driven.
3. For bikes:
   - Select the bike model.
   - Enter the year of manufacture.
   - Enter the kilometers driven.
4. Click the **Predict Price** button to get the estimated price.

## Technology Stack

- **Backend:** Python, Scikit-learn
- **Frontend:** Streamlit
- **Machine Learning Model:** Linear Regression
- **Dataset:** 
  - Cars dataset: `Cleaned_car.csv`
  - Bikes dataset: `Cleaned_bike.csv`

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/your-username/automobile-price-predictor.git
   cd automobile-price-predictor
2.	Install dependencies:

   ```bash
     pip install -r requirements.txt
```````
3.Run the application:
  ```````
  streamlit run app.py
```````
Project Structure:
```````
  automobile-price-predictor/
├── app.py                   # Main application file
├── Cleaned_car.csv          # Dataset for car prices
├── Cleaned_bike.csv         # Dataset for bike prices
├── LinearRegressionModel_Car.pkl  # Trained car price model
├── LinearRegressionModel_Bike.pkl # Trained bike price model
├── requirements.txt         # Python dependencies
└── README.md                # Project documentation
```````
## Deployment on Streamlit Cloud

- This project is deployed on Streamlit Cloud. To deploy it yourself:
	1.	Add all project files to a GitHub repository.
	2.	Ensure requirements.txt is included in the repository.
	3.	Go to Streamlit Cloud and deploy the app by linking your GitHub repository.
	4.	The app will automatically install dependencies and run the app.py file.
