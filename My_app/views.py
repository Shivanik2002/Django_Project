from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return render(request,'Register.html')
def submit_form(request):
    if request.method == "POST":
        First_Name.request.POST["First_Name"]
        Middle_Name.request.POST["Middle_Name"]
        Last_Name.request.POST["Last_Name"]
        Phone_Number.request.POST["Phone_Number"]
        College_Name.request.POST["College_Name"]
        Home_Address.request.POST["Home_Address"]
       
    else:
        return HttpResponse("<h1>404 . Not Found</h1>")