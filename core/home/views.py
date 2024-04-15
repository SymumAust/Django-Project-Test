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

    return render(request, 'index.html', context = {'peoples': peoples})



def success_page(request):
    print('*'*10)
    return HttpResponse("<h1>Hey I'm Django</h1>")
