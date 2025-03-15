from django.contrib import admin
from django.urls import path
from cmsapp.views import home,showdept,adddept,removedept,showstudent,addstudent,removestudent

urlpatterns = [
    path('admin/', admin.site.urls),
    path("",home,name="home"),
    path("showdept",showdept,name="showdept"),
    path("adddept",adddept,name="adddept"),
    path("removedept/<int:id>",removedept,name="removedept"),
    path("showstudent",showstudent,name="showstudent"),
    path("addstudent",addstudent,name="addstudent"),
    path("removestudent/<int:id>",removestudent,name="removestudent"),
]
