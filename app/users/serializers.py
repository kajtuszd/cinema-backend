from rest_framework import serializers

from .models import User


class UserSerializer(serializers.ModelSerializer):
    is_moderator = serializers.BooleanField(read_only=True)

    class Meta:
        model = User
        fields = [
            'first_name',
            'last_name',
            'username',
            'date_joined',
            'phone',
            'email',
            'is_moderator',
        ]
        lookup_field = 'username'
        extra_kwargs = {
            'url': {'lookup_field': 'username'}
        }
