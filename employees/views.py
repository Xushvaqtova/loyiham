from django.shortcuts import render
from django.shortcuts import redirect
from .models import Employee


def employee_list(request):
    employees = Employee.objects.all()
    return render(request, 'list.html', {'employees': employees})


def add_employee(request):
    if request.method == "POST":
        name = request.POST['name']
        position = request.POST['position']
        salary = request.POST['salary']

        Employee.objects.create(
            name=name,
            position=position,
            salary=salary
        )
        return redirect('/')
    return render(request, 'add.html')


def edit_employee(request, id):
    emp = Employee.objects.get(id=id)

    if request.method == "POST":
        emp.name = request.POST['name']
        emp.position = request.POST['position']
        emp.salary = request.POST['salary']
        emp.save()
        return redirect('/')

    return render(request, 'edit.html', {'emp': emp})


def delete_employee(request, id):
    emp = Employee.objects.get(id=id)
    emp.delete()
    return redirect('/')

