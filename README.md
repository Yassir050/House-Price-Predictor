🏠 House Price Predictor

A simple Machine Learning project that predicts house prices based on basic property features.

📌 Overview

House Price Predictor is a beginner-friendly Machine Learning project built with Python and Scikit-learn.

The model uses three features:

* Area — house area in square meters
* Bedrooms — number of bedrooms
* Bathrooms — number of bathrooms

It uses Linear Regression to learn the relationship between these features and the house price.

✨ Features

* Load house price data from CSV
* Clean and prepare the dataset
* Split data into training and testing sets
* Train a Linear Regression model
* Evaluate the model using MAE and R² Score
* Save the trained model with Joblib
* Predict the price of a new house
* Automated training with GitHub Actions

🧠 How It Works

House Price Dataset
        ↓
Data Cleaning
        ↓
Train / Test Split
        ↓
Linear Regression
        ↓
Model Evaluation
        ↓
Save Model
        ↓
Price Prediction

🛠️ Technologies

* Python
* Pandas
* Scikit-learn
* Joblib
* Git & GitHub
* GitHub Actions

📂 Project Structure

House-Price-Predictor/
├── data/
│   └── house_prices.csv
├── src/
│   ├── preprocess.py
│   ├── train.py
│   └── predict.py
├── models/
├── requirements.txt
├── README.md
└── .gitignore

⚙️ Installation

Clone the repository:

git clone https://github.com/Yassir050/House-Price-Predictor.git
cd House-Price-Predictor

Install the required dependencies:

pip install -r requirements.txt

🚀 Train the Model

Run:

python src/train.py

The program will:

1. Load the dataset.
2. Clean the data.
3. Split the dataset.
4. Train the Linear Regression model.
5. Evaluate the model.
6. Save the trained model.

The model will be saved as:

models/house_price_model.pkl

🔮 Make a Prediction

After training the model, run:

python src/predict.py

Enter:

Area (m²)
Number of bedrooms
Number of bathrooms

The program will return the predicted house price.

📊 Model Evaluation

The model is evaluated using:

MAE

Mean Absolute Error measures the average difference between the predicted and actual prices.

R² Score

R² measures how well the model explains the variation in the target values.

🤖 GitHub Actions

The project uses GitHub Actions to automatically run the training process whenever changes are pushed to the main branch.

This provides basic experience with:

* Continuous Integration
* Automated Python workflows
* Automated model training

📚 Skills Practiced

* Python
* Pandas
* Data Cleaning
* Machine Learning
* Linear Regression
* Train/Test Split
* Model Evaluation
* Model Persistence
* Git & GitHub
* GitHub Actions

👨‍💻 Author

Yassir.B

GitHub: Yassir050
