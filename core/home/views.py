from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
def home(request):
    peoples =[
        {'name': 'John', 'age': '16' },
        {'name': 'Robin', 'age': '86' },
        {'name': 'Ej', 'age': '32' },
        {'name': 'ek', 'age': '87' }

    ]
    for people in peoples:
        print(people)
    context ={'page': 'Django Tutorial',
              
               'peoples': 'peoples'}

    return render(request, 'index.html', context)



def success_page(request):
    print('*'*10)
    return HttpResponse("<h1>Hey I'm Django</h1>")

def about(request):
    context ={'page': 'about'}
    return render(request, 'about.html', context)

def contact(request):
    context ={'page': 'contact'}
    return render(request, 'contact.html', context)

def base(request):
    return render(request, 'base.html')
