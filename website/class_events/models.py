from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
from markdownx.models import MarkdownxField
from markdownx.utils import markdownify
import os

def content_file_name(instance,filename):
	ext="png"
	filename= str(instance.title)+"."+str(ext)
	return os.path.join('images/',filename)

class Revents(models.Model):
    title = models.CharField(max_length=30)
    link = models.URLField(null=True,blank=True)
    image = models.ImageField(blank=True, null=True, upload_to=content_file_name)
    start_time = models.DateTimeField(null=True)
    end_time = models.DateTimeField(null=True)
    description = MarkdownxField(null=True,blank=True)
    created_at = models.DateTimeField(auto_now=False, auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True, auto_now_add=False)

    # Create a property that returns the markdown instead
    @property
    def formatted_markdown(self):
        return markdownify(self.description)

    def __str__(self):
        return self.title

    class Meta:
        managed = True
        db_table = 'Revents'
        verbose_name_plural = 'Revents'

class Class(models.Model):
    title = models.CharField(max_length=30)
    year_choices = (
        ('1', 'First Year'),
        ('2', 'Second Year'),
    )
    year = models.CharField(max_length=50, choices=year_choices ,default='1')
    start_time = models.DateTimeField(null=True)
    end_time = models.DateTimeField(null=True)
    link = models.URLField(null=True,blank=True)
    description = MarkdownxField()
    created_at = models.DateTimeField(auto_now=False, auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True, auto_now_add=False)

    # Create a property that returns the markdown instead
    @property
    def formatted_markdown(self):
        return markdownify(self.description)

    def __str__(self):
        return str(self.id) + " " + self.title
    class Meta:
        managed = True
        db_table = 'Class'
        verbose_name_plural = 'Class' 
