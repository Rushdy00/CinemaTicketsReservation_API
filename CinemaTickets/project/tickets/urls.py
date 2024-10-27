from django.urls import path
from .views import *
urlpatterns = [
    path('movies/', MoviesViewOrCreate.as_view(), name='movie-view'),
    path('movies/<int:pk>', MoviesViewUpdateDestroy.as_view(), name='movie-detail'),
]
