from django.shortcuts import render, redirect
from django.db import IntegrityError
from .models import Emp

# Home page
def emp_home(request):
    return render(request, 'emp/home.html', {})

# Add Employee
def add_emp(request):
    if request.method == "POST":
        # Data fetch from form
        emp_name = request.POST.get("emp_name")
        emp_id = request.POST.get("emp_id")
        emp_phone = request.POST.get("emp_phone")
        emp_address = request.POST.get("emp_address")
        emp_working = request.POST.get("emp_working")
        emp_department = request.POST.get("emp_department")

        # Create Emp model object
        e = Emp(
            name=emp_name,
            emp_id=emp_id,
            phone=emp_phone,
            address=emp_address,
            department=emp_department,
            working=emp_working is not None  # Sets True if checkbox checked, False otherwise
        )

        try:
            # Save employee data
            e.save()
            return redirect("/emp/home/")

        except IntegrityError:
            # Handle unique constraint failure for emp_id
            return render(request, 'emp/add_emp.html', {'error': 'Employee ID already exists!'})
    
    return render(request, 'emp/add_emp.html', {})
