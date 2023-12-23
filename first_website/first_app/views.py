from django.shortcuts import render,redirect
from adminpanel.models import student, course
import random
from django.core.mail import send_mail
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


def generate_otp():
    return str(random.randint(100000, 999999))
def login(request):
    if request.method == "POST":
        email = request.POST["email1"]
        
        otp = generate_otp()
          
        send_mail(
            'Subject: Your OTP',
            f'Your OTP is: {otp}',
            'djnagomail@gmail.com',
            [email],
            fail_silently=False,

            )

        # Save the OTP in the session for later validation
        request.session['otp'] = otp
        request.session['email'] = email
        return redirect("validate_otp")


    return render(request,"onlyemail.html")



def validate_otp(request):
    if request.method == 'POST':
        user_entered_otp = request.POST["otp"]
        stored_otp = request.session['otp']
        print(stored_otp)
        email_store = request.session['email']

        print(email_store)
        if user_entered_otp == stored_otp :

            data=student.objects.filter(Email=email_store )
            print(data)
            context={"data":data}
            if len(data) is not 0 :
                print("yes")

                return render(request, "studentdashboard.html",context)

            
            

    return render(request,"onlyotp.html")  # Redirect to the OTP input form
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