# IMDB Sentiment Analysis API

Ushbu loyiha IMDB kino sharhlarini (reviews) tahlil qilish uchun yaratilgan Machine Learning API hisoblanadi.

## Loyiha haqida
- **Model:** Random Forest Classifier
- **Maqsad:** Matnli sharhni ijobiy (positive) yoki salbiy (negative) ekanligini aniqlash.
- **Texnologiyalar:** Python, FastAPI, Scikit-learn, Docker, Render.

## Fayllar tarkibi
- `Model/`: Serializatsiya qilingan model va vectorizer fayllari.
- `main.py`: FastAPI server kodi va `/predict` endpointi.
- `Dockerfile`: Loyihani konteynerga o'rash uchun ko'rsatmalar.
- `requirements.txt`: Kerakli kutubxonalar ro'yxati.

## API-ni ishga tushirish (Local)
1. Docker image-ni qurish: `docker build -t imdb-api .`
2. Konteynerni yurgizish: `docker run -p 10000:10000 imdb-api`
