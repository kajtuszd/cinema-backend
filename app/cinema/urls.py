from rest_framework.routers import DefaultRouter

from . import views

router = DefaultRouter()
router.register(r'movie', viewset=views.MovieViewSet, basename='movie')

urlpatterns = [] + router.urls
