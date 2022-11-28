from rest_framework import generics, viewsets
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from users.permissions import IsModerator

from .models import Hall, Movie, Show, Ticket
from .permissions import IsModeratorOrOwner
from .serializers import (HallSerializer, MovieSerializer, SeatSerializer,
                          ShowSerializer, TicketSerializer)


class MovieViewSet(viewsets.ModelViewSet):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer
    lookup_field = 'slug'

    def get_permissions(self):
        if self.action in ['list', 'retrieve']:
            permission_classes = [IsAuthenticated]
        else:
            permission_classes = [IsModerator]
        return [permission() for permission in permission_classes]


class HallRetrieveDestroyAPIView(generics.RetrieveDestroyAPIView):
    queryset = Hall.objects.all()
    serializer_class = HallSerializer
    permission_classes = [IsModerator,]
    lookup_field = 'hall_number'


class HallListCreateAPIView(generics.ListCreateAPIView):
    queryset = Hall.objects.all()
    serializer_class = HallSerializer
    permission_classes = [IsModerator,]


class ShowViewSet(viewsets.ModelViewSet):
    queryset = Show.objects.all()
    serializer_class = ShowSerializer
    permission_classes = [IsModerator,]
    lookup_field = 'slug'

    def get_permissions(self):
        if self.action in ['list', 'retrieve', 'get_seats']:
            permission_classes = [IsAuthenticated]
        else:
            permission_classes = [IsModerator]
        return [permission() for permission in permission_classes]

    @action(detail=True, methods=['get'])
    def get_seats(self, request, slug):
        show = self.get_object()
        seats_serializer = SeatSerializer(show.seats.all(), many=True)
        return Response(seats_serializer.data)


class TicketViewSet(viewsets.ModelViewSet):
    queryset = Ticket.objects.all()
    serializer_class = TicketSerializer
    permission_classes = [IsModeratorOrOwner,]
    lookup_field = 'slug'

    def get_queryset(self, *args, **kwargs):
        if self.request.user.is_moderator:
            return self.queryset
        return self.queryset.filter(owner=self.request.user)
    
    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)
