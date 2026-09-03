from pathlib import Path

import joblib


BASE_DIR = Path(__file__).resolve().parent.parent
MODEL_PATH = BASE_DIR / "models" / "house_price_model.pkl"


def load_model():
    return joblib.load(MODEL_PATH)


def predict_price(area, bedrooms, bathrooms):
    model = load_model()

    features = [[area, bedrooms, bathrooms]]

    prediction = model.predict(features)[0]

    return prediction


if __name__ == "__main__":
    area = float(input("Enter area (m²): "))
    bedrooms = int(input("Enter number of bedrooms: "))
    bathrooms = int(input("Enter number of bathrooms: "))

    price = predict_price(area, bedrooms, bathrooms)

    print(f"Predicted Price: {price:.2f}")
