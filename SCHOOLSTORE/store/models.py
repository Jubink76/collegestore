from django.db import models


class Department(models.Model):
    name = models.CharField(max_length=100)
    wikipedia_link = models.URLField()

    def __str__(self):
        return self.name 


class Course(models.Model):
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Material(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
    

class MyFormData(models.Model):
    name = models.CharField(max_length=50)
    dob = models.DateField(null=True, blank=True)
    age = models.IntegerField(null=True, blank=True)
    gender = models.CharField(max_length=10, choices=[("male", "Male"), ("female", "Female")])
    phone_number = models.IntegerField(null=True, blank=True)
    mail_id = models.EmailField(null=True, blank=True)
    address = models.TextField(null=True, blank=True)
    department = models.ForeignKey(Department, on_delete=models.CASCADE, null=True, blank=True)
    course = models.ForeignKey(Course, on_delete=models.CASCADE, null=True, blank=True)
    purpose = models.CharField(max_length=20, choices=[("enquiry", "Enquiry"), ("order", "Place Order"), ("return", "Return")])
    materials_provide = models.ManyToManyField(Material, blank=True)

    def __str__(self):
        return self.name

