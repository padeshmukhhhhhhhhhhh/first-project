from django.shortcuts import render
from adminpanel.models import student, course
# Create your views here.
def index(request):

    return render(request,"index.html")
def All(request):

    return render(request,"All.html")
def Path(request):

    return render(request,"Path.html")
def portfolio(request):

    return render(request,"portfolio-details.html")
def service(request):

    return render(request,"services-details.html")
def blog(request):

    return render(request,"blog.html")

def blogdetails(request):

    return render(request,"blog-details1.html")
def login(request):
    if request.method == "POST":
        email = request.POST["email1"]
        
        data=student.objects.filter(Email=email)
        context={"data":data}
        if data is not None:
           print("yes")
           return render(request, "studentdashboard.html",context)
    return render(request,"newlogin.html")

def adminlogin(request):

    return render(request,"adminlogin.html")
def signup(request):

    return render(request,"signup.html")

def contact(request):

    return render(request,"Contact.html")
def events(request):

    return render(request,"events.html")
def gallary(request):

    return render(request,"gallary.html")
def interview(request):

    return render(request,"interview.html")
def offers(request):

    return render(request,"offers.html")
def privacy(request):

    return render(request,"privacy.html")
def search(request):

    return render(request,"search.html")

def sitemap(request):

    return render(request,"sitemap.html")
def terms(request):

    return render(request,"terms.html")
def testimonial(request):

    return render(request,"testimonial.html")
def cert(request):

    return render(request,"verify-cert.html")
def wu(request):

    return render(request,"Why_Unique.html")
def about(request):

    return render(request,"About.html")
def allnew(request):
    new=course.objects.all()
    print(new)
    dict={"new":new}
    return render(request, "allnew.html",dict)

def profile(request):

    return render(request,"profile.html")