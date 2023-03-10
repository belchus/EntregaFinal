from django.urls import include, path
from AppCoder import views
from django.contrib.auth.views import LogoutView


urlpatterns = [
    path('', views.inicio),
    path('movies/', views.Movies),
    path('add_form/', views.add_form, name='add_form'),
    path('favorite/', views.Movies),
    path('fav_form/', views.fav_form, name='fav_form'),
    path('all_reviews/', views.Reviews),
    path('find_movie/', views.find_movie, name='find_movie'),
    path('resultados/',views.Resultados,name='resultados'),
    path('busqueda/',views.Busqueda),
    path('login/',views.login_request),
    path('register/',views.register, name="register"),
    path('logout/',LogoutView.as_view(template_name='logout.html'), name="logout"),
    path('edit-profile/', views.edit_profile, name ='edit-profile'),
    path('edit-avatar/', views.create_avatar, name ='edit-avatar'),
    path('perfil/', views.Perfil ),
    

]
 
