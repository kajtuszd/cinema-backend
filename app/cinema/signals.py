from django.db.models.signals import post_save, pre_save, pre_delete
from django.dispatch import receiver

from .models import Seat, Show, Ticket


@receiver(post_save, sender=Show)
def create_seats(sender, instance, created, **kwargs):
    if created:
        for _ in range(instance.hall.seats_number):
            Seat.objects.create(show=instance)


@receiver(post_save, sender=Ticket)
def free_place(sender, instance, created, **kwargs):
    instance.seat.state = 2
    instance.seat.save()


@receiver(pre_delete, sender=Ticket)
def free_place(sender, instance, using, **kwargs):
    instance.seat.state = 1
    instance.seat.save()


@receiver(pre_save, sender=Ticket)
def reassign_place(sender, instance, **kwargs):
    if instance.id is not None:
        previous = Ticket.objects.get(id=instance.id)
        if previous.seat != instance.seat:
            previous.seat.state = 1
            previous.seat.save()
            instance.seat.state = 2
            previous.seat.save()
