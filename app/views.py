from django.shortcuts import render
from app.forms import *
from django.http import HttpResponse
# Create your views here.

def dforms(request):
    st=student()
    d={'st':st}
    if request.method=="POST":
        fd=student(request.POST)
        if fd.is_valid():
            return HttpResponse(str(fd.cleaned_data))
    return render(request,'forms.html',d)