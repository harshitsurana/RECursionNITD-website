from django.shortcuts import render, redirect,get_object_or_404, get_list_or_404
from .models import *
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from .forms import Eventsform, Classform
from django.conf import settings
from django.utils import timezone
from datetime import timedelta
import datetime
from django.core.exceptions import PermissionDenied

def superuser_only(function):
   def _inner(request, *args, **kwargs):
       if not request.user.is_superuser:
           raise PermissionDenied
       return function(request, *args, **kwargs)
   return _inner

def events(request):
    today=datetime.datetime.now()
    
    current_events=Revents.objects.all().exclude(start_time__gte=today).exclude(end_time__lte=today).order_by('start_time')
    current_class=Class.objects.all().exclude(start_time__gte=today).exclude(end_time__lte=today).order_by('start_time')
    
    upcoming_events=Revents.objects.all().filter(start_time__gte=today).order_by('start_time')
    upcoming_class=Class.objects.all().filter(start_time__gte=today).order_by('start_time')
    
    past_events=Revents.objects.all().filter(end_time__lte=today).order_by('-start_time')
    past_class=Class.objects.all().filter(end_time__lte=today).order_by('-start_time')
    
    context={
        'ce':current_events,
        'cc':current_class,
        'pe':past_events,
        'pc':past_class,
        'ue':upcoming_events,
        'uc':upcoming_class
    }
    return render(request, 'class_events/class_events.html',context)

@superuser_only
def revent_create(request):
    perms=0
    if request.user.is_superuser:
        perms=1

    form = Eventsform(request.POST,request.FILES or None)
    if form.is_valid():

        form.save()
        return redirect('class_events:events')

    return render(request, 'class_events/create_revent.html',{'form':form,"perms":perms})

@superuser_only
def class_create(request):
    perms=0
    if request.user.is_superuser:
        perms=1

    form = Classform(request.POST or None)
    print(form)
    if form.is_valid():
        form.save()
        return redirect('class_events:events')

    return render(request, 'class_events/create_class.html',{'form':form,"perms":perms})

@superuser_only
def class_update(request,id):
    try:
        event =get_object_or_404(Class, pk=id)

    except:
        return HttpResponse("id does not exist")
    else:
        perms=0
        if request.user.is_superuser:
            perms=1
        else:
            return HttpResponse("Go get perms,only admins")
        upform = Classform(request.POST or None, instance=event)

        if request.method == "POST":
            if upform.is_valid():

                upform.save()
                return redirect('class_events:events')
        return render(request, 'class_events/update_class.html',{'upform':upform,"perms":perms})

@superuser_only
def revent_update(request,id):
    try:
        event =get_object_or_404(Revents, pk=id)

    except:
        return HttpResponse("id does not exist")
    else:
        perms=0
        if request.user.is_superuser:
            perms=1
        else:
            return HttpResponse("Go get perms,only admins")
        upform = Eventsform(request.POST,request.FILES or None, instance=event)

        if request.method == "POST":
            if upform.is_valid():

                upform.save()
                return redirect('class_events:events')
        return render(request, 'class_events/update_event.html',{'upform':upform,"perms":perms})

def class_detail(request,id):
    try:
        event = get_object_or_404(Class,pk=id)
    except:
        return HttpResponse("id does not exist")
    else:
        return render(request,'class_events/class_detail.html',{'class':event})

def revent_detail(request,id):
    try:
        event = get_object_or_404( Revents,pk=id)
    except:
        return HttpResponse("id does not exist")
    else:
        return render(request,'class_events/revent_detail.html',{'event':event})
