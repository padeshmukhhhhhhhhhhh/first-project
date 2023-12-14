from django.urls import path
from . import views
urlpatterns = [
    path('',views.index,name="index"),
    path('All',views.All,name="All"),
    path('Path',views.Path,name="Path"),
    path('portfolio',views.portfolio,name="portfolio"),
    path('service',views.service,name="service"),
    path('blog',views.blog,name="blog"),
    path('blogdetails',views.blogdetails,name="blogdetails"),
    path('login',views.login,name="login"),
    path('signup',views.signup,name="signup"),
    path('contact',views.contact,name="contact"),
    path('events',views.events,name="events"),
    path('gallary',views.gallary,name="gallary"),
    path('interview',views.interview,name="interview"),
    path('offers',views.offers,name="offers"),
    path('privacy',views.privacy,name="privacy"),
    path('search',views.search,name="search"),
    path('sitemap',views.sitemap,name="sitemap"),
    path('terms',views.terms,name="terms"),
    path('testimonial',views.testimonial,name="testimonial"),
    path('cert',views.cert,name="cert"),
    path('wu',views.wu,name="wu"),
     path('about',views.about,name="about"),
]