from django.http import HttpResponse
from django.shortcuts import render

def start(request):
    return render(request,'index.html')
def class10(request):
    return render(request,'static/class10/10.html')
def class9(request):
    return render(request,'static/class9/9.html')
def class8(request):
    return render(request,'static/class1-8/8.html')
def contact(request):
    return render(request,'static/contact_us/contact.html')