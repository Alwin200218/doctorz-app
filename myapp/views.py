from django.shortcuts import render,redirect
from .models import Userdata,Doctorinfo,Appointmentinfo
from django.contrib import messages
# Create your views here.

def index(request):
    return render(request,'index.html')


def signup(request,method=['GET','POST']):
    if request.method == "POST":
        email=request.POST.get('email')
        password1=request.POST.get('password1')
        password2=request.POST.get('password2')

        user=Userdata.objects.filter(email=email)

        if user.exists():
            messages.info(request,"User is already exists")
        elif password1 != password2:
            messages.info(request,"Password does not match") 
        else:
            Userdata.objects.create(email=email,password=password1)
            return render(request,'login.html')       
            
        
    return render(request,'signup.html')


def login(request):
     if request.method == "POST":
        email=request.POST.get('email')
        password1=request.POST.get('password1')

        user=Userdata.objects.filter(email=email,password=password1)

        if user.exists():
            return redirect("/home/")
            
     return render(request,'login.html')


def home(request):
    doctors=Doctorinfo.objects.all()
    return render(request,'main.html',{'doctors':doctors})


def register(request,id):
    doctor=Doctorinfo.objects.get(id=id)

    return render(request,'form.html',{'doctor':doctor})


def doctorRegister(request):
     if request.method == 'POST':
        doctor_name=request.POST.get('doctor_name') 
        pname=request.POST.get('pname') 
        page=request.POST.get('page') 
        pemail=request.POST.get('pemail') 
        pcontactno=request.POST.get('pcontactno') 
        desc=request.POST.get('desc') 
        Appointmentinfo.objects.create(doctor=doctor_name,name=pname,age=page,email=pemail,contactno=pcontactno,desc=desc)
        return render(request,'success.html')





