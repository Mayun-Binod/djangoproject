from django.http import HttpResponse
from django.shortcuts import render
import datetime

def home(request):
    isActive = True  # Default value
    
    if request.method == "POST":
        check = request.POST.get('check')  # Safely getting value with .get()
        print(f"Checkbox value: {check}")
        if check is None:
            isActive = False  # Checkbox not checked, make isActive False
        else:
            isActive = True  # Checkbox checked, make isActive True
    
    date = datetime.datetime.now()
    name = "LearnWithBinodSir"
    list_of_programs = [
        "WAP to check even or odd",
        "WAP to check prime number",
        "WAP to print all prime numbers from 1 to 100",
        "WAP to print pascals triangle"
    ]
    student = {
        "student_name": "Binod",          
        "student_college": "Swoyambhu International College",
        "student_city": "Lalitpur"
    }
    data = {
        "date": date,
        "isActive": isActive,
        "name": name,
        "list_of_programs": list_of_programs,
        "student_data": student
    }
    return render(request, "home.html", data)

def about(request):
    return render(request, "about.html", {})

def services(request):
    return render(request, "services.html", {})
