from flask import Flask, render_template, request
import numpy as np
import pickle

app = Flask(__name__)

# Load trained model
model = pickle.load(open("model.pkl", "rb"))

@app.route('/')
def home():
    return render_template("index.html")

@app.route('/predict', methods=['POST'])
def predict():

    # Get values from form
    anxiety_level = float(request.form['anxiety_level'])
    self_esteem = float(request.form['self_esteem'])
    mental_health_history = float(request.form['mental_health_history'])
    depression = float(request.form['depression'])
    headache = float(request.form['headache'])
    blood_pressure = float(request.form['blood_pressure'])
    sleep_quality = float(request.form['sleep_quality'])
    breathing_problem = float(request.form['breathing_problem'])
    noise_level = float(request.form['noise_level'])
    living_conditions = float(request.form['living_conditions'])
    safety = float(request.form['safety'])
    basic_needs = float(request.form['basic_needs'])
    academic_performance = float(request.form['academic_performance'])
    study_load = float(request.form['study_load'])
    teacher_student_relationship = float(request.form['teacher_student_relationship'])
    future_career_concerns = float(request.form['future_career_concerns'])
    social_support = float(request.form['social_support'])
    peer_pressure = float(request.form['peer_pressure'])
    extracurricular_activities = float(request.form['extracurricular_activities'])
    bullying = float(request.form['bullying'])

    # Put all inputs in correct order
    input_data = np.array([[anxiety_level, self_esteem, mental_health_history,
                            depression, headache, blood_pressure,
                            sleep_quality, breathing_problem, noise_level,
                            living_conditions, safety, basic_needs,
                            academic_performance, study_load,
                            teacher_student_relationship,
                            future_career_concerns, social_support,
                            peer_pressure, extracurricular_activities,
                            bullying]])

    # Prediction
    prediction = model.predict(input_data)[0]

    return render_template("index.html",
                           prediction_text=f"Predicted Stress Level: {prediction}")

if __name__ == "__main__":
    app.run(debug=True)