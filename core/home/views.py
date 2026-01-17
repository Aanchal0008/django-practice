from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def home_view(request):
    text = "It's my home page"
    names = ['Amit', 'Sumit', 'Ramesh', 'Suresh']
    # names = []
    # return HttpResponse("<h1>Welcome to the home page!</h1>")
    return render(request, 'index.html', context={"abcd":text, "names":names})

def project(request):
    dct = {"Name":"Ansh", "Roll_No":103, "Percentage":56.3}

    names = ['Amit', 'Sumit', 'Ramesh', 'Suresh']
    # return HttpResponse("<h3>Project</h3>\n<p>aaj gaye project pe....</p>")
    return render(request, 'project.html', context={'dict':dct, 'names':names})

def about(request):
    return render(request, 'about.html')