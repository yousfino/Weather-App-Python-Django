# 🌤️ Weather Air Quality App (Django)

Welcome to the **Weather Air Quality App**, a simple yet insightful web application that lets users check the current air quality index (AQI) in various locations based on ZIP codes. Built with **Python** and the **Django** web framework, this project demonstrates how to consume and display data from a third-party API in a dynamic web application.

## 📌 Features

- 🔍 Search by ZIP code to get real-time air quality data.
- 📊 Displays AQI values and their corresponding health category (e.g., Good, Moderate, Hazardous).
- 🎨 Color-coded interface based on AQI category.
- 🌐 Connects to the **AirNow API** to fetch live data.
- 🧠 Basic logic to interpret and display user-friendly air quality descriptions.

## 🛠️ Technologies Used

- Python 3
- Django Web Framework
- HTML/CSS (for basic templates)
- [AirNow API](https://www.airnowapi.org/) for live air quality data

## 🚀 How It Works

1. The app defaults to a preset ZIP code (e.g., Las Vegas).
2. Users can enter a different ZIP code into the search bar.
3. The app sends a request to the AirNow API using the provided ZIP code.
4. Based on the AQI value returned, the app displays:
   - The numeric score
   - A health category (e.g., "Good", "Moderate", "Hazardous")
   - A color-coded background and a brief description of the health implications

## 🧪 Example

- ZIP Code: `89129` (Las Vegas)
  - AQI: `43`
  - Category: `Good`
  - Description: _"Enjoy your outdoor activities."_

- ZIP Code: `63101` (St. Louis)
  - AQI: `100`
  - Category: `Moderate`
  - Description: _"If you are unusually sensitive to ozone, consider reducing your activity level."_

## 🧑‍💻 Learnings from the Project

- How to integrate **third-party APIs** in Django
- How to process JSON responses and apply conditional logic
- Rendering dynamic content in Django templates
- Basics of handling POST requests with forms in Django

## ⚙️ Getting Started

1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/Weather-App-Python-Django.git
   cd Weather-App-Python-Django

2. Set up a virtual environment:
    ```
    python -m venv weatherapp
    source weatherapp/bin/activate  # On Windows: weatherapp\Scripts\activate
    ```
3. Install requirements:
    ```
    pip install -r requirements.txt
    ```
4. Run the development server:
   ```
   python manage.py runserver
   ``` 
5. Open in browser: `http://127.0.0.1:8000/`

## 🔐 API Key
This project uses the [AirNow API](https://www.airnowapi.org/). You must [sign up](https://docs.airnowapi.org/login?index=) to get your free API key and replace the placeholder key in the code.

## Enjoy 😉
