from django.shortcuts import render
from django.http import JsonResponse
from .forms import MyForm
from .models import Department, Course
from django.contrib import messages


def home(request):
    departments = Department.objects.all()
    print(departments)
    return render(request, 'home.html',{'departments':departments})

def dashboard(request):
    return render(request, 'dashboard.html')

def show_form(request):
    if request.method == 'POST':
        form = MyForm(request.POST)
        if form.is_valid():
            form.save()
        messages.success(request, 'Order Confirmed')

    else:
        form = MyForm()

    return render(request, 'form_template.html', {'form': form})

def get_courses(request):
    department_id = request.GET.get('department_id')
    print(department_id)
    if department_id:
        # Filter courses based on the selected department
        courses = Course.objects.filter(department=department_id).values('id', 'name')
    else:
        # Return an empty list if no department is selected
        courses = []

    # Convert the queryset to a list of dictionaries
    courses_list = list(courses)
    return JsonResponse({'courses': courses_list})