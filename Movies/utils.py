import requests
from .models import Movie

def search_movies(query):
    api_key = 'f0ab8b81'
    url = f'http://www.omdbapi.com/?apikey={api_key}&s={query}'
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        movies = data.get('Search', [])
        for movie in movies:
            imdb_id = movie.get('imdbID')
            movie_details_url = f'http://www.omdbapi.com/?apikey={api_key}&i={imdb_id}'
            details_response = requests.get(movie_details_url)
            if details_response.status_code == 200:
                movie_details = details_response.json()
                year_str = movie_details.get('Year', '')
                if '–' in year_str:
                    year_str = year_str.split('–')[0]
                try:
                    year = int(year_str)
                except ValueError:
                    year = None

                if year is not None:
                    poster_url = movie_details.get('Poster', '')
                    if poster_url == 'N/A':
                        poster_url = ''  # Set empty string if poster URL is 'N/A'
                    Movie.objects.update_or_create(
                        title=movie_details.get('Title', ''),
                        defaults={
                            'year': year,
                            'genre': movie_details.get('Genre', ''),
                            'plot': movie_details.get('Plot', ''),
                            'poster_url': poster_url,
                        }
                    )
                movie.update(movie_details)
        return movies
    else:
        return []