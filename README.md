# 🔥 Forest Fire Prediction

This is a simple machine learning web app built using **Flask** to predict the chance of a forest fire based on input values like temperature, humidity, wind speed, and rainfall.


## how to use this website
first click on the deployed link : https://test-forest-fire-2.onrender.com/
the website will look like this :

<img width="1919" height="1079" alt="image" src="https://github.com/user-attachments/assets/11dad58d-9caf-4fe6-b030-90fc07cb72a6" />


This is the Predicted Data :

<img width="1919" height="870" alt="image" src="https://github.com/user-attachments/assets/2f0c8e56-46dc-4f1a-b66e-d37949cf07df" />



## 🚀 Features

- Input values through a web form
- Predicts whether a forest fire is likely or not
- Uses a trained ML model (`forest_fire.pkl`)

## 🧠 Model Input Parameters

- Temperature (°C)
- Relative Humidity (%)
- Wind Speed (km/h)
- Rainfall (mm)

## 📁 Project Structure

test_forest_fire/
├── static/
├── templates/
│ └── index.html
├── app.py
├── forest_fire.pkl
|__ requirements.txt



## ⚙️ How to Run

1. Clone the repo:
2. git clone https://github.com/Mayank-Pandey-Ji/test_forest_fire.git
3. cd test_forest_fire

4. (Optional) Create virtual environment:
5. python -m venv venv
6. venv\Scripts\activate # On Windows
7. pip install -r requirements.txt
8. Run the app:python app.py
