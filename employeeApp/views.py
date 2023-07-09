from django.shortcuts import render, HttpResponse
from django.shortcuts import render
from .models import Employee, Role, Department
from datetime import datetime
from django.db.models import Q


def index(request):
    return render(request, "index.html", {})


def addEmp(request):
    if request.method == "POST":
        firstName = request.POST["firstName"]
        lastName = request.POST["lastName"]
        dept = request.POST["dept"]
        role = request.POST["role"]
        phone = int(request.POST["phone"])
        salary = int(request.POST["salary"])
        bonus = int(request.POST["bonus"])

        new_emp = Employee(
            firstName=firstName,
            lastName=lastName,
            dept_id=dept,
            role_id=role,
            phone=phone,
            salary=salary,
            bonus=bonus,
            joiningDate=datetime.now(),
        )

        new_emp.save()

        return HttpResponse("Employee Added Successfully")

    elif request.method == "GET":
        return render(request, "addEmp.html")

    else:
        return HttpResponse("Exception Occured")


def remEmp(request, empId=0):
    if empId:
        try:
            employeeToBeRemoved = Employee.objects.get(id=empId)
            employeeToBeRemoved.delete()
            return HttpResponse("Employee Removed succesfully")
        except:
            return HttpResponse("Please enter valid employee id")

    emps = Employee.objects.all()
    context = {"emps": emps}

    return render(request, "remEmp.html", context)


def viewEmp(request):
    emps = Employee.objects.all()
    context = {"emps": emps}

    return render(request, "viewEmp.html", context)


def filterEmp(request):
    if request.method == "POST":
        name = request.POST["name"]
        dept = request.POST["dept"]
        role = request.POST["role"]
        emps = Employee.objects.all()

        if name:
            emps = emps.filter(
                Q(firstName__icontains=name) | Q(lastName__icontains=name)
            )
        if dept:
            emps = emps.filter(dept__name__contains=dept)
        if role:
            emps = emps.filter(role__name__contains=role)

        context = {"emps": emps}

        return render(request, "viewEmp.html", context)

    elif request.method == "GET":
        return render(request, "filterEmp.html")

    else:
        return HttpResponse("An error occured")
