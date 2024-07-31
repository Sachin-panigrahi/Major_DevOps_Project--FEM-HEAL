"""
URL configuration for Female_Healthcare_Management project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.urls import path, include
from female_healthcare_management.views import *
from django.conf import settings
from django.contrib.auth import views as auth_views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',home,name="HOMEPAGE"),
    path('Impressum/',imprint,name="IMPRINT"),
   path('doctors/', doctor_list, name='doctor_list'),
    path('doctors/<int:doctor_id>/', doctor_detail, name='doctor_detail'),
    path('doctors/<int:doctor_id>/location/', doctor_location, name='doctor_location'),
    path('physical_health/',physical_health,name="Physical-Health-Issues"),
    path('mental_health/',mental_health,name="Physical-Health-Issues"),
    path('menstrual_health/',menstrual_health,name="Physical-Health-Issues"),
    path('customer_reviews/',customer_reviews,name="Customer_Reviews"),
    path('health/',health,name="Customer_Reviews"),
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', CustomLogoutView.as_view(), name='logout'), 
    path('login/', CustomLoginView.as_view(template_name='login.html'), name='login'),
    # path('login/',login,name="login_page"),
    path('register/',register,name="register_page"),
    # path('accounts/', include('accounts.urls')), 

]
from django.conf.urls.static import static
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)