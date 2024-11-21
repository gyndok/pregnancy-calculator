# Pregnancy Calculator

A web application that helps calculate pregnancy dates and gestational age using either Last Menstrual Period (LMP) or ultrasound information.

## Features

- Calculate gestational age and due date using Last Menstrual Period (LMP)
- Calculate gestational age and due date using ultrasound measurements
- Clean, modern interface with two calculation methods
- Instant results with no page reload

## Installation

1. Clone this repository
2. Create a virtual environment (recommended):
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install the required packages:
```bash
pip install -r requirements.txt
```

## Running the Application

1. Activate the virtual environment if you haven't already:
```bash
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

2. Run the Flask application:
```bash
python app.py
```

3. Open your web browser and navigate to `http://localhost:5000`

## Usage

### LMP Method
1. Select the "LMP Method" tab
2. Enter the date of the last menstrual period
3. Click "Calculate" to see the current gestational age and due date

### Ultrasound Method
1. Select the "Ultrasound Method" tab
2. Enter the ultrasound date
3. Enter the gestational age in weeks and days as measured during the ultrasound
4. Click "Calculate" to see the current gestational age and due date
