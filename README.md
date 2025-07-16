# 🔥 Forest Fire Prediction

This is a simple machine learning web app built using **Flask** to predict the chance of a forest fire based on input values like temperature, humidity, wind speed, and rainfall.


## how to use this website
first click on the deployed link : https://test-forest-fire-2.onrender.com/
the website will look like this :

![Screenshot 2025-06-27 123807](https://github.com/user-attachments/assets/475bf9c6-aeb1-4054-b2b1-99d50931ca4c)


Now add/write predictdata in the url section , like this:

![Screenshot 2025-06-27 123819](https://github.com/user-attachments/assets/3e09899e-6ef9-4648-8133-10a2231f585e)

now you can predict the data :

![Screenshot 2025-06-27 123829](https://github.com/user-attachments/assets/f2d08b82-ac42-487c-9bb7-f6bca5f9515d)


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
