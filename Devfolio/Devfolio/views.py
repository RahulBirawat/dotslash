import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from django.shortcuts import render

def home(request):
    return render(request, "home.html")

def predict(request):
    return render(request, "predict.html")

def predict_1(request):
    return render(request, "predict_1.html")

def predict_2(request):
    return render(request, "predict_2.html")

def result(request):
    # Read data from CSV file
    data = pd.read_csv(r"C:\Users\91941\Desktop\Dotslash\jhbfvdjsb\JHBFVDJSB\JHBFVDJSB\diabetes.csv")

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
    data = pd.read_csv(r"C:\Users\91941\Desktop\Dotslash\jhbfvdjsb\JHBFVDJSB\JHBFVDJSB\heart.csv")

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
    data = pd.read_csv(r"C:\Users\91941\Desktop\Dotslash\jhbfvdjsb\JHBFVDJSB\JHBFVDJSB\lung_cancer.csv")

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
