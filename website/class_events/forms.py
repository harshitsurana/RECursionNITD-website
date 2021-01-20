from django import forms
from .models import *
from markdownx.fields import MarkdownxFormField
from markdownx.utils import markdownify

class Eventsform(forms.ModelForm):
    title = models.CharField(max_length=30)
    link = models.URLField()
    description = models.TextField()
    description = MarkdownxFormField()
    start_time = forms.DateTimeField()
    end_time = forms.DateTimeField() 

    def clean_description(self):
        data = self.cleaned_data['description']
        data = markdownify(data)
        return data

    class Meta:
        model=Revents
        fields=('title','link','description','image','start_time','end_time')

class Classform(forms.ModelForm):
    title = models.CharField(max_length=30)
    year_choices = (
        ('1', 'First Year'),
        ('2', 'Second Year'),
    )
    year = models.CharField(max_length=50, choices=year_choices ,default='1')
    link = models.URLField()
    description = models.TextField()
    description = MarkdownxFormField()
    start_time = forms.DateTimeField()
    end_time = forms.DateTimeField()  

    def clean_description(self):
        data = self.cleaned_data['description']
        data = markdownify(data)
        return data

    class Meta:
        model=Class
        fields=('title','year','link','description','start_time','end_time')