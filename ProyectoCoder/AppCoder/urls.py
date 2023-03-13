from django.urls import include, path
from AppCoder import views
from django.contrib.auth.views import LogoutView
from AppCoder.views import *
from django.conf import settings

urlpatterns = [
 path('', views.inicio),
    path('movies/', views.Movies),
    path('add_form/', views.add_form),
    path('all_movies/', views.Movies),
    path('find_movie/', views.find_movie, name='find_movie'),
    path('resultados/',views.Resultados,name='resultados'),
    path('busqueda/',views.Busqueda),
    path('login/',views.login_request,name="login"),
    path('logout/', LogoutView.as_view(template_name='logout.html'),name='logout'),
    path('register/',views.register, name="register"),
    path('logout/',LogoutView.as_view(template_name='logout.html'), name="logout"),
    path('edit-profile/', views.edit_profile, name ='edit-profile'),
    path('edit-avatar/', views.create_avatar, name ='edit-avatar'),
    path('all_reviews/', views.all_reviews ,name ='all_reviews'),
    path('detail_reviews/<pk>', views.detail_reviews, name='detail_reviews'),
    path('review_form/', views.review_form, name='review_form'),
    path('delete_review/<pk>', views.delete_review, name='delete_review'),
    path('update_review/<pk>', views.update_review, name='update_review'),
    path('delete_reply/<pk>', views.delete_reply, name='delete-reply'),
    path('revdetail/<pk>', views.detail_reviews, name='revdatail'),



]

handler400 = Error_404.as_view()
 
