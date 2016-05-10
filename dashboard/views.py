from django.shortcuts import render

# Create your views here.

def dashboard(request):
    ''' dashboard'''
    return render(request,'dashboard/dashboard.html')
