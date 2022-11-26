from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework.generics import RetrieveDestroyAPIView, ListCreateAPIView
from users.permissions import IsModerator

from .models import Movie, Hall
from .serializers import MovieSerializer, HallSerializer


class MovieViewSet(viewsets.ModelViewSet):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer
    lookup_field = 'slug'

    def get_permissions(self):
        print(self.action)
        if self.action in ['list', 'retrieve']:
            permission_classes = [IsAuthenticated]
        else:
            permission_classes = [IsModerator]
        return [permission() for permission in permission_classes]


class HallRetrieveDestroyAPIView(RetrieveDestroyAPIView):
    queryset = Hall.objects.all()
    serializer_class = HallSerializer
    permission_classes = [IsModerator,]
    lookup_field = 'hall_number'


class HallListCreateAPIView(ListCreateAPIView):
    queryset = Hall.objects.all()
    serializer_class = HallSerializer
    permission_classes = [IsModerator,]
