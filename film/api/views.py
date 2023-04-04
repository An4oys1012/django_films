from django.shortcuts import render
from django.views.generic.base import View
from .models import Movie, Category, Actor, Genre, Rating, Reviews


class MoviesView(ListView):
    """Список фильмов"""
    model = Movie
    template_name = "movies/movie_list.html


class MovieDetailView(DetailView):
    """Полное описание фильма"""
    model = Movie
    slug_field = "url"
