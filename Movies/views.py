from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, authenticate
from .utils import search_movies
from .forms import MovieListForm
from .models import MovieList, Movie
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponseRedirect
import random

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'Movies/signup.html', {'form': form})

@login_required

def home(request):
    movies = []
    if 'q' in request.GET:
        query = request.GET.get('q')
        if query:
            movies = search_movies(query)
    return render(request, 'Movies/home.html', {'movies': movies})


# @login_required
# def home(request):
#     movies = []
#     query = request.GET.get('q', '')
#     if query:
#         movies = search_movies(query)
    
#     # Fetch random movies from the OMDB API
#     suggestions = []
#     for _ in range(5):
#         random_letter = chr(random.randint(97, 122)) 
#         random_movies = search_movies(random_letter)
#         if random_movies:
#             random_movie = random.choice(random_movies)
#             suggestions.append(random_movie)
    
#     return render(request, 'Movies/home.html', {'movies': movies, 'query': query, 'suggestions': suggestions})

def movie_search(request):
    movies = []
    if 'q' in request.GET:
        query = request.GET.get('q')
        if query:
            # Search movies using OMDB API
            movies = search_movies(query)
    return render(request, 'Movies/movie_search.html', {'movies': movies})
    
    
def view_public_movie_list(request, list_id):
    # Fetch the public movie list by its ID
    movie_list = get_object_or_404(MovieList, id=list_id, privacy='public')
    return render(request, 'Movies/public_movie_list.html', {'movie_list': movie_list})


@login_required
def your_movies(request):
    if request.method == 'POST':
        action = request.POST.get('action')
        selected_movies = request.POST.getlist('selected_movies')

        if action == 'edit':
            # Handle edit action (if needed)
            pass
        elif action == 'delete':
            # Delete selected movies
            for movie_id in selected_movies:
                movie = get_object_or_404(Movie, id=movie_id)
                movie.delete()

    # Fetch movies associated with the user's default movie list
    movie_list = get_object_or_404(MovieList, user=request.user, title="Default")
    movies = movie_list.movies.all()

    return render(request, 'Movies/your_movies.html', {'movies': movies})


@login_required
def create_movie_list(request):
    if request.method == 'POST':
        form = MovieListForm(request.POST)
        if form.is_valid():
            movie_list = form.save(commit=False)
            movie_list.user = request.user
            movie_list.save()
            return redirect('your_movies')
    else:
        form = MovieListForm()
    return render(request, 'Movies/create_movie_list.html', {'form': form})


@login_required
def edit_movie_list(request, list_id):
    movie_list = get_object_or_404(MovieList, id=list_id, user=request.user)
    if request.method == 'POST':
        form = MovieListForm(request.POST, instance=movie_list)
        if form.is_valid():
            form.save()
            return redirect('your_movies')
    else:
        form = MovieListForm(instance=movie_list)
    return render(request, 'Movies/edit_movie_list.html', {'form': form})


@login_required
def delete_movie_list(request, list_id):
    movie_list = get_object_or_404(MovieList, id=list_id, user=request.user)
    if request.method == 'POST':
        movie_list.delete()
        return redirect('your_movies')
    return render(request, 'Movies/delete_movie_list.html', {'movie_list': movie_list})


@login_required
def add_movie(request):
    """
    View function to add a movie directly to the user's default movie list.
    """
    if request.method == 'POST':
        title = request.POST.get('title')
        year = request.POST.get('year')
        genre = request.POST.get('genre')
        plot = request.POST.get('plot')
        
        movie = Movie.objects.create(title=title, year=year, genre=genre, plot=plot)
        
        # Get or create the user's default movie list
        movie_list, created = MovieList.objects.get_or_create(user=request.user, title="Default")
        
        movie_list.movies.add(movie)
        
        return HttpResponseRedirect('/your_movies/') 
    else:
        pass

@login_required
def add_to_movie_list(request, movie_id):
    """
    View function to allow the user to select a specific movie list to add a movie.
    """
    if request.method == 'POST':
        movie_list_id = request.POST.get('movie_list_id')
        
        movie_list = get_object_or_404(MovieList, pk=movie_list_id, user=request.user)
        movie = get_object_or_404(Movie, pk=movie_id)
        
        movie.movie_list = movie_list
        movie.save()
        
        return redirect('movie_search') 
    else:
        movie_lists = MovieList.objects.filter(user=request.user)
        return render(request, 'Movies/add_to_movie_list.html', {'movie_lists': movie_lists})