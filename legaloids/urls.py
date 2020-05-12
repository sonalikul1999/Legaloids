from django.contrib import admin
from django.urls import path
from app.views import *
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',index),
    path('preloader/',preloader),
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
    path('saveblog/',saveblog),
    path('team/',team),
    path('sendquote/',sendquote),
    path('delete/',deleteblog),
    path('adminhome/',adminhome),
    path('adminlogout/',adminlogout),
    path('downloaddata/',downloaddata),
    path('industries/',industries),
    path('careers/',careers),
]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

if settings.DEBUG:
        urlpatterns += static(settings.MEDIA_URL,
                              document_root=settings.MEDIA_ROOT)