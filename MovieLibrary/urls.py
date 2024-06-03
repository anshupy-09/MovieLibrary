"""
URL configuration for MovieLibrary project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.contrib.auth import views as auth_views
from Movies import views as movies_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/', auth_views.LoginView.as_view(template_name='Movies/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='/login/'), name='logout'),
    path('signup/', movies_views.signup, name='signup'),
    path('home/', movies_views.home, name='home'),
    path('', auth_views.LoginView.as_view(template_name='Movies/login.html'), name='login'),
    path('movie_search/', movies_views.movie_search, name='movie_search'),
    path('movie-list/<int:list_id>/', movies_views.view_public_movie_list, name='view_public_movie_list'),
    path('your_movies/', movies_views.your_movies, name='your_movies'),
    path('create-movie-list/', movies_views.create_movie_list, name='create_movie_list'),
    path('edit-movie-list/<int:list_id>/', movies_views.edit_movie_list, name='edit_movie_list'),
    path('delete-movie-list/<int:list_id>/', movies_views.delete_movie_list, name='delete_movie_list'),
    # path('add-to-movie-list/<int:movie_id>/', movies_views.add_to_movie_list, name='add_to_movie_list'),
    path('add_movie/', movies_views.add_movie, name='add_movie'),

]
