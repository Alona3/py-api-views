from django.urls import path, include

from rest_framework.routers import DefaultRouter
from cinema.views import (
    GenreListCreateAPIView,
    GenreDetailAPIView,
    ActorListCreateView,
    ActorDetailView,
    CinemaHallViewSet,
    MovieViewSet
)

router = DefaultRouter()
router.register(r'cinema-halls', CinemaHallViewSet, basename='cinema-hall')
router.register(r'movies', MovieViewSet, basename='movie')

urlpatterns = [
   path('genres/', GenreListCreateAPIView.as_view(), name='genre-list-create'),
    path('genres/<int:pk>/', GenreDetailAPIView.as_view(), name='genre-detail'),

    path('actors/', ActorListCreateView.as_view(), name='actor-list-create'),
    path('actors/<int:pk>/', ActorDetailView.as_view(), name='actor-detail'),

    path('', include(router.urls)),
]

app_name = "cinema"
