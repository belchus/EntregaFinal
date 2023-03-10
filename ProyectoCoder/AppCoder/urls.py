from django.urls import include, path
from AppCoder import views
from django.contrib.auth.views import LogoutView
from django.conf import settings

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
    path('reviews/', views.all_reviews, name='all-posts'),
    path('review-detail/<pk>', views.detail_reviews, name='post-detail'),
    path('review-form', views.review_form, name='post-form'),
    path('delete-review/<pk>', views.delete_review, name='delete-post'),
    path('update-review/<pk>', views.update_review, name='update-post'),
    path('delete-reply/<pk>', views.delete_reply, name='delete-comment'),



]
 
