from django.shortcuts import render

# Create your views here.

def count(request):
    return render(request,'count.html')
