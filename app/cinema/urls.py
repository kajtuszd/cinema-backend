from django.urls import path
from rest_framework.routers import DefaultRouter

from . import views

router = DefaultRouter()
router.register(r'movies', viewset=views.MovieViewSet, basename='movie')

urlpatterns = [
    path('halls/', views.HallListCreateAPIView.as_view(), name='user_list_create_view'),
    path('halls/<int:hall_number>/', views.HallRetrieveDestroyAPIView.as_view(), name='user_retrieve_destroy_view'),
] + router.urls
