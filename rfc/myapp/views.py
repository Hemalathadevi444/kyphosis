from django.shortcuts import render
import pickle
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
import pandas as pd
from sklearn.tree import DecisionTreeClassifier
from django.http import HttpResponse
from rfc.settings import BASE_DIR

# Create your views here.


def myview(request):
    if request.method == "POST":
        age = float(request.POST["age"])
        number_of_curves = float(request.POST["number_of_curves"])
        vertebraes_involved_in_it = float(
            request.POST["vertebraes_involved_in_it"])
        model = pickle.load(
            open(BASE_DIR/"rfc/decision_tree_pickle.pkl", "rb"))
        return render(request, "result.html", {"status": 0 if model.predict([[age, number_of_curves, vertebraes_involved_in_it]])[0] == "absent" else 1})

    return render(request, "main.html")
