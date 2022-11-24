from rest_framework.generics import ListAPIView
from rest_framework.permissions import IsAuthenticated

from users.models import User

from .serializers import UserSerializer
from .permissions import IsModerator


class UserListView(ListAPIView):
    queryset = User.objects.all()
    permission_classes = [IsAuthenticated, IsModerator]
    serializer_class = UserSerializer
