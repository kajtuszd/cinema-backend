from datetime import date
from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from users.models import User
from utils.slugs import generate_slug


def get_current_year():
    return date.today().year


def max_value_current_year(value):
    return MaxValueValidator(get_current_year())(value)


SEAT_STATES = (
    (1, ("Free")),
    (2, ("Reserved"))
)


class Movie(models.Model):
    title = models.CharField(max_length=50, blank=False)
    production_year = models.PositiveIntegerField(default=get_current_year(),
                                                  validators=[
                                                      MinValueValidator(1950),
                                                      max_value_current_year])
    time_in_minutes = models.PositiveIntegerField(blank=False, validators=[
        MaxValueValidator(300)])
    description = models.CharField(max_length=200, blank=True, null=True)
    slug = models.CharField(default=generate_slug, max_length=10,
                            unique=True, db_index=True, editable=False)

    def __str__(self):
        return f"{self.title} ({self.production_year})"

    class Meta:
        unique_together = (
            'title', 'production_year', 'time_in_minutes', 'description',)


class Hall(models.Model):
    hall_number = models.PositiveIntegerField(blank=False, unique=True)
    seats_number = models.PositiveIntegerField(blank=False, default=50,
                                               validators=[
                                                   MaxValueValidator(200)])
    slug = models.CharField(default=generate_slug, max_length=10,
                            unique=True, db_index=True, editable=False)

    def __str__(self):
        return f"{self.hall_number} ({self.seats_number} places)"


class Show(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    hall = models.ForeignKey(Hall, on_delete=models.CASCADE)
    start_time = models.DateTimeField(null=True)
    slug = models.CharField(default=generate_slug, max_length=10,
                            unique=True, db_index=True, editable=False)

    def __str__(self):
        return f"{self.movie}"


class Seat(models.Model):
    show = models.ForeignKey(Show, on_delete=models.CASCADE, null=True)
    state = models.IntegerField(choices=SEAT_STATES, default=1)
    slug = models.CharField(default=generate_slug, max_length=10,
                            unique=True, db_index=True, editable=False)

    def __str__(self):
        return f"{self.slug}"


class Ticket(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    seat = models.OneToOneField(Seat, on_delete=models.CASCADE, null=True)
    price = models.PositiveIntegerField(default=20,
                                        validators=[MaxValueValidator(100)])
    slug = models.CharField(default=generate_slug, max_length=10,
                            unique=True, db_index=True, editable=False)

    def __str__(self):
        return f"{self.slug}"
