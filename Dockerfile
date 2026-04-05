FROM python:3.9-slim

WORKDIR /app

# Avval kutubxonalarni o'rnatamiz (Keshdan samarali foydalanish uchun)
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# BU YERDA XATO BOR EDI: Endi hamma fayllarni nusxalaymiz
COPY . .

# Render tekin rejasi uchun 10000 porti tavsiya etiladi
EXPOSE 10000

# Kodni ishga tushirish (main.py ichidagi 'app' obyektini qidiradi)
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "10000"]