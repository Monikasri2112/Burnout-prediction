# Burnout Prediction System

## Overview
The Burnout Prediction System is a web-based application designed to assess an individual's burnout level based on key lifestyle and workload indicators such as sleep duration, working hours, and stress levels. The system leverages a machine learning model to provide early insights into burnout risk, helping users take preventive measures.

---

## 🚀 Live Demo

https://burnout-prediction-production.up.railway.app

---

## Features
- Predicts burnout levels: Low, Moderate, or High
- User-friendly web interface for input collection
- Real-time prediction using a Flask-based backend
- Lightweight and fast response system
- Scalable architecture for future enhancements

---

## Technology Stack

**Frontend**
- HTML
- CSS
- JavaScript

**Backend**
- Python
- Flask

**Machine Learning**
- Scikit-learn 
- Trained classification model

---

## System Architecture

```
Client (Browser)
      ↓
Frontend (HTML/CSS/JavaScript)
      ↓
Flask API (Backend Server)
      ↓
Machine Learning Model
      ↓
Prediction Response
      ↓
Display on User Interface
```

---

## Working Principle

1. The user provides input parameters such as sleep hours, work/study duration, and stress level.
2. The frontend sends this data to the Flask backend via HTTP requests.
3. The backend preprocesses the input and passes it to the trained machine learning model.
4. The model evaluates the input and predicts the burnout level.
5. The prediction result is returned and displayed on the user interface.

---

## Project Structure

```
burnout-prediction/
│
├── static/               # Frontend assets (CSS, JavaScript)
├── templates/            # HTML templates
├── model/                # Serialized ML model
├── app.py                # Flask application
├── requirements.txt      # Project dependencies
└── README.md             # Documentation
```

---

## Installation and Setup

1. Clone the repository:
```
git clone https://github.com/your-username/burnout-prediction.git
cd burnout-prediction
```

2. Install required dependencies:
```
pip install -r requirements.txt
```

3. Run the application:
```
python app.py
```

4. Access the application:
```
http://127.0.0.1:5000/
```

---

## Input Parameters

- Sleep Duration (hours)
- Work/Study Duration (hours)
- Stress Level and some more

---

## Output

The system classifies burnout into one of the following categories:
- Low
- Moderate
- High

---

## Future Enhancements
- Improved model accuracy with larger datasets
- Deployment on cloud platforms for public access

---

## 👨‍💻 Author

**MONIKA SRI K**  
- GitHub: https://github.com/Monikasri2112  
- LinkedIn: https://www.linkedin.com/in/monika-sri-k-494674292/
