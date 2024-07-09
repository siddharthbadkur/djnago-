from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import redirect


# # Create your views here.
# def home(request):
#     return HttpResponse("this is my home  page")
# def home(request):
#     return render(request,"home.html")
def home(request):
    return redirect("https://www.youtube.com/")
