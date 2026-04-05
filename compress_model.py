import joblib
# Modelni yuklash
model = joblib.load("Model/rf_model.pkl")
# Modelni siqilgan holda qayta saqlash (9 - eng yuqori siqish darajasi)
joblib.dump(model, "Model/rf_model.pkl", compress=9)
print("Model muvaffaqiyatli siqildi!")