from django.db.models.signals import post_save
from django.dispatch import receiver

from .models import Seat, Show


@receiver(post_save, sender=Show)
def create_seats(sender, instance, created, **kwargs):
    if created:
        for _ in range(instance.hall.seats_number):
            Seat.objects.create(show=instance)
