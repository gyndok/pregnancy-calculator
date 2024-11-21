from flask import Flask, render_template, jsonify, request
from datetime import datetime, timedelta
from dateutil.relativedelta import relativedelta

app = Flask(__name__)

def calculate_gestational_age(from_date):
    today = datetime.now().date()
    days_difference = (today - from_date).days
    weeks = days_difference // 7
    remaining_days = days_difference % 7
    return weeks, remaining_days

def calculate_due_date(lmp_date):
    return lmp_date + relativedelta(days=280)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/calculate_from_lmp', methods=['POST'])
def calculate_from_lmp():
    lmp_date = datetime.strptime(request.json['lmp'], '%Y-%m-%d').date()
    weeks, days = calculate_gestational_age(lmp_date)
    due_date = calculate_due_date(lmp_date)
    
    return jsonify({
        'gestational_age': f"{weeks} weeks and {days} days",
        'due_date': due_date.strftime('%m/%d/%Y')
    })

@app.route('/calculate_from_ultrasound', methods=['POST'])
def calculate_from_ultrasound():
    us_date = datetime.strptime(request.json['ultrasoundDate'], '%Y-%m-%d').date()
    ga_weeks = int(request.json['gaWeeks'])
    ga_days = int(request.json['gaDays'])
    
    # Calculate the implied LMP date
    total_days = ga_weeks * 7 + ga_days
    implied_lmp = us_date - timedelta(days=total_days)
    
    # Calculate current gestational age and due date
    weeks, days = calculate_gestational_age(implied_lmp)
    due_date = calculate_due_date(implied_lmp)
    
    return jsonify({
        'gestational_age': f"{weeks} weeks and {days} days",
        'due_date': due_date.strftime('%m/%d/%Y')
    })

if __name__ == '__main__':
    app.run(debug=True, port=5001)
