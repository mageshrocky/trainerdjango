from django import forms
from .models import Trainer, Details


class Vtrainer(forms.ModelForm):
    name = forms.CharField(max_length=30)
    email = forms.EmailField(max_length=30)
    password = forms.CharField(max_length=10)
    role = forms.CharField(max_length=30)

    class Meta:
        model = Trainer
        fields = {'name', 'email', 'password', 'role'}


class Vdetails(forms.ModelForm):
    trainer_name = forms.CharField(max_length=30)
    student_name = forms.CharField(max_length=30)
    mob_no = forms.CharField(max_length=10)
    course = forms.CharField(max_length=30)
    duration = forms.CharField(max_length=30)
    time_slot = forms.CharField(max_length=10)

    class Meta:
        model = Details
        fields = {'trainer_name', 'student_name', 'mob_no', 'course', 'duration', 'time_slot'}
