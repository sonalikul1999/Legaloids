from django.contrib import admin
from django.urls import path
from app.views import *
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',index),
    path('about/',about),
    path('blog/',blog),
    path('casedetails/',casedetails),
    path('contact/',contact),
    path('elements/',elements),
    path('index/',index),
    path('services/',services),
    path('singleblog/',singleblog),
    path('study/',study),
    path('adminpannel/',adminpannel),
    path('adminlogin/',adminlogin),
    path('postblog/',postblog),
    path('allblogs/',allblogs),

    path('analytics/',analytics),

    path('error/',error),

]
