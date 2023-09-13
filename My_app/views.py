from django.shortcuts import render
from django.http import HttpResponse
from My_app.models import Register

# Create your views here.
def index(request):
    return render(request,'Register.html')
def submit_form(request):
    if request.method == "POST":
        First_Name=request.POST["First_Name"]
        Middle_Name=request.POST["Middle_Name"]
        Last_Name=request.POST["Last_Name"]
        Phone_Number=request.POST["Phone_Number"]
        College_Name=request.POST["College_Name"]
        Home_Address=request.POST["Home_Address"]
        Gender=request.POST["Gender"]
        Area_Prog=request.POST.get("Programming","off")
        Area_Sing=request.POST.get("Singing","off")
        Area_Danc=request.POST.get("Dancing","off")
        Area_Stud=request.POST.get("Studying","off")
        Area_play=request.POST.get("Playing","off")
        AOI=[]
        if Area_Prog == "Programming":
            AOI.append(Area_Prog)
        if Area_Sing == "Singing":
             AOI.append(Area_Sing)
        if Area_Danc == "Dancing":
             AOI.append(Area_Danc)
        if Area_Stud == "Studying":
             AOI.append(Area_Stud)
        if Area_play == "Playing":
             AOI.append(Area_play)

        print(First_Name,Middle_Name,Last_Name,Phone_Number,College_Name,Gender,*AOI)  
        Register( First_Name= First_Name,Middle_Name=Middle_Name,Last_Name=Last_Name,Phone_Number=Phone_Number,College_Name=College_Name,Home_Address=Home_Address,Gender=Gender,Area_of_intrest=AOI).save()
        msg = "From Submitted Successfully" 
        return render(request,'Register.html',{'msg':msg})  
       
    else:
        return HttpResponse("<h1>404 . Not Found</h1>")