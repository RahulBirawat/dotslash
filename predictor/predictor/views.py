import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from django.shortcuts import render
import requests

def home(request):
    return render(request, "home.html")

def predict(request):
    return render(request, "predict.html")

def predict_1(request):
    return render(request, "predict_1.html")

def predict_2(request):
    return render(request, "predict_2.html")

def form(request):
    return render(request, "form.html")

import os
from django.conf import settings

def result(request):
    # Read data from CSV file
    BASE_DIR = settings.BASE_DIR  # Get the project's base directory
    DATA_DIR = os.path.join(BASE_DIR, 'predictor/diabetes.csv')  # Construct relative path

    data = pd.read_csv(DATA_DIR)

    # Separate features (x) and target (y)
    x = data.drop("Outcome", axis=1)
    y = data['Outcome']

    # Split data into training and testing sets
    x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2)

    # Initialize and train logistic regression model
    model = LogisticRegression()
    model.fit(x_train, y_train)

    # Get input values from request
    val1 = float(request.GET['n1'])
    val2 = float(request.GET['n2'])
    val3 = float(request.GET['n3'])
    val4 = float(request.GET['n4'])
    val5 = float(request.GET['n5'])
    val6 = float(request.GET['n6'])
    val7 = float(request.GET['n7'])
    val8 = float(request.GET['n8'])

    # Make prediction
    pred = model.predict([[val1, val2, val3, val4, val5, val6, val7, val8]])

    # Determine result
    if pred == 1:
        result1 = "Positive"
    else:
        result1 = "Negative"

    # Render predict.html template with result
    return render(request, "predict.html", {"result2": result1})




def result_1(request):
    # Read data from CSV file
    BASE_DIR = settings.BASE_DIR  # Get the project's base directory
    DATA_DIR = os.path.join(BASE_DIR, 'predictor/heart.csv')  # Construct relative path

    data = pd.read_csv(DATA_DIR)

    # Separate features (x) and target (y)
    x = data.drop("Outcome", axis=1)
    y = data['Outcome']

    # Split data into training and testing sets
    x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.3)

    # Initialize and train logistic regression model
    model = LogisticRegression()
    model.fit(x_train, y_train)

    # Get input values from request
    val1 = float(request.GET['n1'])
    val2 = float(request.GET['n2'])
    val3 = float(request.GET['n3'])
    val4 = float(request.GET['n4'])
    val5 = float(request.GET['n5'])
    val6 = float(request.GET['n6'])
    val7 = float(request.GET['n7'])
    val8 = float(request.GET['n8'])
    val9 = float(request.GET['n9'])
    val10 = float(request.GET['n10'])
    val11 = float(request.GET['n11'])
    val12 = float(request.GET['n12'])

    # Make prediction
    pred = model.predict([[val1, val2, val3, val4, val5, val6, val7, val8,val9, val10,val11,val12]])

    # Determine result
    if pred == 0:
        result1 = "Normal Heart"
    elif pred == 1:
        result1 = "Fixed Heart Defect"
    else:
        result1 = "Reversable Heart Defect"

    # Render predict.html template with result
    return render(request, "predict_1.html", {"result2": result1})




def result_2(request):
    # Read data from CSV file
    BASE_DIR = settings.BASE_DIR  # Get the project's base directory
    DATA_DIR = os.path.join(BASE_DIR, 'predictor/lung_cancer.csv')  # Construct relative path

    data = pd.read_csv(DATA_DIR)

    # Separate features (x) and target (y)
    x = data.drop("Outcome", axis=1)
    y = data['Outcome']

    # Split data into training and testing sets
    x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2)

    # Initialize and train logistic regression model
    model = LogisticRegression()
    model.fit(x_train, y_train)

    # Get input values from request
    val1 = float(request.GET['n1'])
    val2 = float(request.GET['n2'])
    val3 = float(request.GET['n3'])
    val4 = float(request.GET['n4'])
    val5 = float(request.GET['n5'])
    val6 = float(request.GET['n6'])
    val7 = float(request.GET['n7'])
    val8 = float(request.GET['n8'])
    val9 = float(request.GET['n9'])
    val10 = float(request.GET['n10'])
    val11 = float(request.GET['n11'])
    val12 = float(request.GET['n12'])

    # Make prediction
    pred = model.predict([[val1, val2, val3, val4, val5, val6, val7, val8,val9, val10,val11,val12]])

    # Determine result
    if pred == 'Low':
        result1 = "Low"
    elif pred == "High":
        result1 = "High"
    else:
        result1 = "Medium"

    # Render predict.html template with result
    return render(request, "predict_2.html", {"result2": result1})

from django.shortcuts import render

import requests

import json
from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def recommender(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        location = data.get('location')
        specialization = data.get('specialization')
        
        # Load doctors data from a local file (assuming it's in JSON format)
        with open('doctors_data.json', 'r') as file:
            doctors_data = json.load(file)

        print(doctors_data)
        
        # Extract doctors matching the user's criteria
        recommended_doctors = []
        for doctor in doctors_data:
            if doctor['location'] == location and doctor['specialization'] == specialization:
                recommended_doctors.append({
                    'name': doctor['name'],
                    'specialty': doctor['specialization'],
                    'location': doctor['location']
                })
                # Limiting to at least four recommendations
                if len(recommended_doctors) >= 4:
                    break
        
        
        # Return JSON response with the list of recommended doctors
        return JsonResponse({'doctors': recommended_doctors})
        
    else:
        # Handle GET request
        return render(request, 'form.html')



    


