"""ProyectoCoder URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.urls import include, path
from AppCoder.views import *
from AppCoder import views
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', inicio),
    path('movies/', views.Movies),
    path('add_form/', views.add_form, name='add_form'),
    path('favorite/', views.Movies),
    path('fav_form/', views.fav_form, name='fav_form'),
    path('reviews/', views.Reviews),
    path('review_form/', views.review_form, name='review_form'),
    path('find_movie/', views.find_movie, name='find_movie'),
    path('resultados/',views.Resultados,name='resultados'),
    path('busqueda/',views.Busqueda),
    path('login/',views.login_request),
    path('register/',views.register, name="register"),
    path('logout/',LogoutView.as_view(template_name='logout.html'), name="logout"),
    path('all_reviews/', views.Reviews),
    path('edit-profile/', views.edit_profile, name ='edit-profile'),
    path('edit-avatar/', views.create_avatar, name ='edit-avatar'),


]
