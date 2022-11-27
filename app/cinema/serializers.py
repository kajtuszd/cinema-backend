from rest_framework import serializers

from .models import Hall, Movie, Seat, Show


class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = [
            'title',
            'production_year',
            'time_in_minutes',
            'description',
            'slug',
        ]
        lookup_field = 'slug'
        extra_kwargs = {
            'url': {'lookup_field': 'slug'}
        }


class HallSerializer(serializers.ModelSerializer):
    class Meta:
        model = Hall
        fields = [
            'hall_number',
            'seats_number',
        ]
        lookup_field = 'hall_number'
        extra_kwargs = {
            'url': {'lookup_field': 'hall_number'}
        }


class SeatSerializer(serializers.ModelSerializer):
    class Meta:
        model = Seat
        fields = [
            'show',
            'state',
            'slug',
        ]


class ShowSerializer(serializers.ModelSerializer):
    class Meta:
        model = Show
        fields = [
            'movie',
            'hall',
            'start_time',
            'slug',
        ]
        lookup_field = 'slug'
        extra_kwargs = {
            'url': {'lookup_field': 'slug'}
        }
