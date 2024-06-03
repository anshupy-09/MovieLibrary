from django import forms
from .models import MovieList


class MovieListForm(forms.ModelForm):
    class Meta:
        model = MovieList
        fields = ['title', 'description', 'privacy']
        
class AddToMovieListForm(forms.Form):
    movie_title = forms.CharField(widget=forms.HiddenInput())