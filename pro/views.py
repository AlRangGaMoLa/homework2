from django.shortcuts import render, redirect

def home(request):
    return redirect('/blog/')
def home2(request):
    return render(request,'home.html')