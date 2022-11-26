from rest_framework.generics import ListAPIView, RetrieveUpdateAPIView

from users.models import User

from .permissions import IsModerator, IsModeratorOrOwner
from .serializers import UserSerializer


class UserListView(ListAPIView):
    queryset = User.objects.all()
    permission_classes = [IsModerator]
    serializer_class = UserSerializer


class UserDetailView(RetrieveUpdateAPIView):
    queryset = User.objects.all()
    permission_classes = [IsModeratorOrOwner]
    serializer_class = UserSerializer
    lookup_field = 'username'
