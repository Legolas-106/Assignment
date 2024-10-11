from django.shortcuts import render
from django.http import JsonResponse
from .forms import *
import json

# Create your views here.

APP_FEATURES = {
    "E-commerce" : ['Product Listing','Payment Integration'],
    "Social Media" : ["User Profiles", "Chat System"],
    "Cloud Kitchen" : ['Menu Display','Online Ordering']
}

hours = {
    "Product Listing" : 30,
    "Payment Integration" : 25,
    "User Profiles" : 30,
    "Chat System" : 40,
    "Menu Display" : 25,
    "Online Ordering" : 40
}

def homePage(request):
    if request.method == 'GET':
        form = AppForm()
        return render(request,'appCalc.html',{"form" : form,"features": APP_FEATURES})
    

def get_cost(request):
    print("POST request is called")
    params = json.loads(request.body)
    print(params)
    app_category = params.get("appCategory")
    app_features = params.get("appFeatures")

    total_hours = 0
    for items in app_features:
        if items not in APP_FEATURES[app_category]:
            return JsonResponse({"success":False,"error":"The given choices are invalid"})
        total_hours += hours[items]

    return JsonResponse({"success":True,"cost" : str(total_hours*10)})
