from django.urls import path
from . import views
urlpatterns = [
   
    
    path("adminpanel",views.adminpanel, name="adminpanel" ),
    path("adddata",views.adddata,name="adddata"),
    path("addcourse",views.addcourse,name="addcourse"),
    path("update/<int:id>",views.update,name="update"),
    path("updatecourse/<int:id>",views.updatecourse,name="updatecourse"),
    path("deletecourse/<int:id>",views.deletecourse,name="deletecourse"),
    path("delete/<int:id>",views.delete,name="delete")
]
