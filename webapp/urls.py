

from django.contrib import admin
from django.urls import path
from webapp import views as webappviews

urlpatterns = [
    #path('admin/', admin.site.urls),
     path("admin/",webappviews.hompage,name="myhomepage"),
     path("",webappviews.webapp_homepage,name="myindex"),
     path("contact",webappviews.web_contact,name="mycontact"),


]