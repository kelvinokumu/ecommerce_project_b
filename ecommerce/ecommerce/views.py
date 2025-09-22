from django.shortcuts import render


def home(request):
    # process the request/fetch data
    return render(request,"home.html")


def about(request):
    # process the request/fetch data
    return render(request,"about.html")