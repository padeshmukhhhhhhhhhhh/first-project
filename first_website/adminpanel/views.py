
from django.shortcuts import render,redirect
from .models import student,course
# Create your views here.



  
def adminpanel(request):
    stud=student.objects.all()
    newdata=course.objects.all() 
    dict={ "stud":stud,
          "newdata":newdata
                }
    print(dict)
    return render(request,"admin.html",dict)

def adddata(request):
    data=student.objects.all(),
   # newdata=course.objects.all() "newdata":newdata
    dict={"data":data,
               }
    
   
    if request.method == "POST":
        print("post")
        name=request.POST['name']
        mobile=request.POST['mobile']
        email=request.POST['email']
        dob=request.POST['dob']
        course=request.POST['course']
        
        newuser=student(name=name,mobile=mobile,Email=email,dob=dob,course=course)
        newuser.save()
        return redirect("adminpanel")   
    
def update(request,id):
    if request.method=="POST":
        name=request.POST['name']
        mobile=request.POST['mobile']
        email=request.POST['email']
        dob=request.POST['dob']
        course=request.POST['course']
        
        newuser=student(id=id,name=name,mobile=mobile,Email=email,dob=dob,course=course)
        newuser.save()
        return redirect("adminpanel")

def delete(request,id):
    if request.method=="POST":
        data=student.objects.filter(id=id)
        data.delete()
        return redirect("adminpanel")   


def addcourse(request):
    data=student.objects.all(),
    newdata=course.objects.all() 
    dict={"data":data,
           "newdata":newdata    }
    
   
    if request.method == "POST":
        print("post")
        title=request.POST['title']
        description=request.POST['description']
        duration=request.POST['duration']
        timing=request.POST['timing']
        course1=request.POST['course']
        
        newuser=course(title=title, description=description,duration=duration,timing=timing,course=course1)
        newuser.save()
        return redirect("adminpanel")   

def updatecourse(request,id):
    if request.method=="POST":
        title=request.POST['title']
        description=request.POST['description']
        duration=request.POST['duration']
        timing=request.POST['timing']
        course1=request.POST['course']
        
        newuser=course(id=id,title=title, description=description,duration=duration,timing=timing,course=course1)
        newuser.save()
        return redirect("adminpanel")

def deletecourse(request,id):
    if request.method=="POST":
        data=course.objects.filter(id=id)
        data.delete()
        return redirect("adminpanel")     