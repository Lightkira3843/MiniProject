from django.contrib import admin
from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static



urlpatterns = [
    path('', views.index,name="home" ),
    path('category/', views.category,name="category" ),
    path('contactus/', views.contactus,name="contactus" ),
    path('login/', views.login,name="login" ),
    path('profile/', views.profile,name="profile" ),
    path('services/', views.services,name="services" ),
    path('courses/', views.courses,name="courses" ),

] # +static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)

