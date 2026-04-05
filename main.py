from fastapi import FastAPI
import joblib
import pandas as pd

app = FastAPI()


try:
    model = joblib.load("Model/rf_model.pkl")
    vectorizer = joblib.load("Model/vectorizer.pkl")
    print("Muvaffaqiyatli: Model va Vectorizer yuklandi!")
except FileNotFoundError:
    print("Xatolik: Model fayllari topilmadi! 'Model/' papkasini tekshiring.")
except Exception as e:
    print(f"Kutilmagan xatolik: {e}")

@app.get("/")
def home():
    return {"message": "IMDB Sentiment Analysis API tayyor!"}

@app.get("/predict")
def predict(text: str):
    if not text.strip():
        return {"error": "Iltimos, matn kiriting!"}

    transformed_text = vectorizer.transform([text])
    
    prediction = model.predict(transformed_text)

    sentiment = "Positive" if int(prediction[0]) == 1 else "Negative"
    
    return {
        "input_text": text,
        "sentiment": sentiment,
        "status": "success"
    }