# MovieLibrary
MovieLibrary is a web application built with Django, designed to help users discover and track their favorite movies. Users can search for movies, view detailed information, and add them to personalized lists.

# Table of Contents
[About](URL)
[Features](URL)
[Installation](URL)
[Usage](URL)
[Contributing](URL)
[License](URL)

# Features
User authentication (signup and login)
Search for movies by title
View detailed information about movies
Add movies to a personalized list
Responsive design 

# Installation
1. Clone the repository:
   
  git clone https://github.com/yourusername/MovieLibrary.git
  cd MovieLibrary
  
3. Create and activate the virtual enviroment :
   
  python -m venv env
  env\Scripts\activate   # On mac use `source env/bin/activate`
  
5. Install dependancies:
   
   pip install -r requirements.txt
   
6. Set up enviroment variable:

   SECRET_KEY=your_secret_key
   ALLOWED_HOSTS=localhost 127.0.0.1
   OMDB_API_KEY=your_omdb_api_key

7.Apply migrations:

  python manage.py makemigrations
  python manage.py migrate

8. Run the developement server:

  python manage.py runserver

9. Open your browser and visit:

  http://127.0.0.1:8000

# Usage
1. Sign up or Log in:
Access the application at http://127.0.0.1:8000.
Sign up for a new account or log in if you already have one.

2. Search for Movies:
Use the search bar on the homepage to search for movies by title.

3.View Movie Details:
Click on a movie from the search results to view its detailed information, including the plot, genre, year, country, cast, and

