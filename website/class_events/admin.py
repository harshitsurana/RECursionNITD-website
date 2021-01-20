from django.contrib import admin
from .models import *

@admin.register(Revents)    
class ReventAdmin(admin.ModelAdmin):
    pass

@admin.register(Class)    
class ClassAdmin(admin.ModelAdmin):
    pass