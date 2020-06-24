from django import forms
from django.forms import ModelForm


from .models import *


class TaskForm(forms.ModelForm):
    title = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Add new task...'}))
    class Meta:
        db_table = ''
        managed = True
        verbose_name = 'ModelName'
        verbose_name_plural = 'ModelNames'

        
        model = Tasks
        fields = '__all__'


