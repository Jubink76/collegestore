from django import forms
from .models import MyFormData

class MyForm(forms.ModelForm):
    class Meta:
        model = MyFormData
        fields = '__all__'
        widgets = {
            'materials_provide': forms.CheckboxSelectMultiple(),
            'department': forms.Select(attrs={'id': 'department-selector'}),  # Add id here
            'course': forms.Select(attrs={'id': 'course-selector'}),  # Add id here
            'dob': forms.DateInput(attrs={'type': 'date'}),

        }
