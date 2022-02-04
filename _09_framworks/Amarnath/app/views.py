from django.shortcuts import render
from django.http import HttpResponse
from .models import Documents


def main(request):
    post = Documents.objects.all()
    return render(request, "main.html", {'post': post})
