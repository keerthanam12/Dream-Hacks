from django.shortcuts import render

def home(request):
    return render(request, "managementsystem/index.html")


def register(request):
    return render(request, "managementsystem/register.html")
