from django.contrib import admin
from django.urls import path,re_path
from MovieApp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('addmovie/', views.add_movie_view),
    path('listmovies/', views.list_movie_view),
    re_path('^.*$', views.index_view),
]
