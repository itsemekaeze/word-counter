from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def index(request):
    return render(request, 'index.html')


def counter(request):
    text = request.POST['text']
    amount = len(text.split())

    context = {
        "amount": amount
    }

    return render(request, 'counter.html', context)