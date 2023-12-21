from django.urls import path
from . import views
urlpatterns = [
    path('studentdashboard',views.studentdashboard,name="studentdashboard"),
    
]