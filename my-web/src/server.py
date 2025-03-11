import sys
import os
import platform
from flask import Flask, render_template, request
from flask import Flask, render_template, redirect, url_for

# Add the parent directory to the Python path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))

from app import healthcare_chatbot

app = Flask(__name__, template_folder='templates', static_folder='static')

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/chatbot', methods=['GET', 'POST'])
def chatbot():
    if request.method == 'POST':
        user_input = request.form['user_input']
        response = healthcare_chatbot(user_input)
        return render_template('chatbot.html', user_input=user_input, response=response)
    return render_template('chatbot.html')

@app.route('/assistant', methods=['GET', 'POST'])
def assistant():
        return redirect("http://localhost:8501") # Adjust port if needed

@app.route('/reminder', methods=['GET', 'POST'])
def reminder():
    if request.method == 'POST':
        medication_name = request.form['medication_name']
        reminder_time = request.form['reminder_time']
        # Here you can add logic to save the reminder
        return render_template('reminder.html', medication_name=medication_name, reminder_time=reminder_time, success=True)
    return render_template('reminder.html')

@app.route('/appointment', methods=['GET', 'POST'])
def appointment():
    if request.method == 'POST':
        name = request.form['name']
        date = request.form['date']
        time = request.form['time']
        # Here you can add logic to save the appointment
        return render_template('appointment.html', name=name, date=date, time=time, success=True)
    return render_template('appointment.html')

if __name__ == "__main__":
    if platform.system() == "Windows":
        app.run(debug=True, use_reloader=False)
    else:
        app.run(debug=True)