from django.shortcuts import render
from django.http import HttpResponse


def home(request):
    return render(request, "forms.html")


def main(request):
    return render(request, "main.html", {"name": "Viveka"})
