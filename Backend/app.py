from flask import Flask, render_template, request, redirect, session
import numpy as np
import pickle
import mysql.connector
import os

app = Flask(__name__, template_folder="../Frontend/templates")

app.secret_key = "burnoutiq_secret_2024"

import os

if os.environ.get("MYSQLHOST"):  
    # 🚀 Railway (production)
    db = mysql.connector.connect(
        host=os.environ.get('MYSQLHOST'),
        user=os.environ.get('MYSQLUSER'),
        password=os.environ.get('MYSQLPASSWORD'),
        database=os.environ.get('MYSQLDATABASE'),
        port=int(os.environ.get('MYSQLPORT', 3306))
    )
else:
    # 💻 Local (your system)
    db = mysql.connector.connect(
        host="localhost",
        user="root",
        password="Monika_21",
        database="burnout_db"
    )


cursor = db.cursor()
print("Database connected successfully")

model = pickle.load(open("../model/model.pkl", "rb"))

@app.route('/')
def home():
    if 'user_id' not in session:
        return redirect('/login')
    return render_template("index.html", username=session.get('user_name'))

@app.route("/login")
def login_page():
    if 'user_id' in session:
        return redirect('/')
    return render_template("login.html")

@app.route("/login", methods=["POST"])
def login():
    email    = request.form["email"]
    password = request.form["password"]
    cursor.execute("SELECT * FROM users WHERE email=%s AND password=%s", (email, password))
    user = cursor.fetchone()
    if user:
        session['user_id']    = user[0]
        session['user_name']  = user[1]
        session['user_email'] = user[2]
        return redirect('/')
    return render_template("login.html", error="Invalid email or password!")

@app.route("/register")
def register_page():
    if 'user_id' in session:
        return redirect('/')
    return render_template("register.html")

@app.route("/register", methods=["POST"])
def register():
    name     = request.form["name"]
    email    = request.form["email"]
    password = request.form["password"]
    cursor.execute("SELECT * FROM users WHERE email=%s", (email,))
    existing = cursor.fetchone()
    if existing:
        return render_template("register.html", error="Email already registered!")
    cursor.execute(
        "INSERT INTO users (name, email, password) VALUES (%s, %s, %s)",
        (name, email, password)
    )
    db.commit()
    return redirect("/login")

@app.route("/logout")
def logout():
    session.clear()
    return redirect("/login")

@app.route("/history")
def history():
    if 'user_id' not in session:
        return redirect('/login')
    cursor.execute(
        "SELECT * FROM predictions WHERE user_id=%s ORDER BY created_at DESC",
        (session['user_id'],)
    )
    data = cursor.fetchall()
    return render_template("history.html", data=data, username=session.get('user_name'))

@app.route('/predict', methods=['POST'])
def predict():
    if 'user_id' not in session:
        return redirect('/login')

    anxiety_level          = int(request.form['anxiety_level'])
    self_esteem            = int(request.form['self_esteem'])
    mental_health_history  = int(request.form['mental_health_history'])
    depression             = int(request.form['depression'])
    sleep_quality          = int(request.form['sleep_quality'])
    academic_performance   = int(request.form['academic_performance'])
    study_load             = int(request.form['study_load'])
    future_career_concerns = int(request.form['future_career_concerns'])
    social_support         = int(request.form['social_support'])
    peer_pressure          = int(request.form['peer_pressure'])

    input_data = np.array([[anxiety_level, self_esteem, mental_health_history,
                            depression, sleep_quality, academic_performance,
                            study_load, future_career_concerns,
                            social_support, peer_pressure]])

    prediction = model.predict(input_data)[0]

    if prediction == 0:
        result = "Low Stress"
    elif prediction == 1:
        result = "Moderate Stress"
    else:
        result = "High Stress"

    cursor.execute("""
        INSERT INTO predictions (
            user_id, anxiety_level, self_esteem, mental_health_history, depression,
            sleep_quality, academic_performance, study_load,
            future_career_concerns, social_support, peer_pressure, stress_level
        ) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)
    """, (
        session['user_id'],
        anxiety_level, self_esteem, mental_health_history, depression,
        sleep_quality, academic_performance, study_load,
        future_career_concerns, social_support, peer_pressure, result
    ))
    db.commit()

    return render_template("result.html",
        prediction_text=f"Predicted Stress Level: {result}",
        username=session.get('user_name')
    )
#if __name__ == "__main__":
    #app.run(debug=True)
if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8080))
    app.run(host="0.0.0.0", port=port)