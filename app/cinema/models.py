from django.utils import timezone
from datetime import date
from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from users.models import User
from utils.slugs import append_slug
from django_extensions.db.fields import AutoSlugField


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
    production_year = models.PositiveIntegerField(default=get_current_year(), validators=[MinValueValidator(1950), max_value_current_year])
    time_in_minutes = models.PositiveIntegerField(blank=False, validators=[MaxValueValidator(300)])
    description = models.CharField(max_length=200, blank=True, null=True)

    def __str__(self):
        return f"{self.title} '('{self.production_year}')'"

    class Meta:
        unique_together = ('title', 'production_year', 'time_in_minutes', 'description',)


class Hall(models.Model):
    hall_number = models.PositiveIntegerField(blank=False, unique=True)
    seats_number = models.PositiveIntegerField(blank=False, default=50, validators=[MaxValueValidator(200)])
    slug = AutoSlugField(populate_from=[str('hall')], db_index=True,
                        unique=True, slugify_function=append_slug)

    def __str__(self):
        return f"{self.slug}"


class Show(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    hall = models.ForeignKey(Hall, on_delete=models.CASCADE)
    start_time = models.DateTimeField(null=True)
    slug = AutoSlugField(populate_from=[str('show')], db_index=True,
                        unique=True, slugify_function=append_slug)
    
    def __str__(self):
        return f"{self.slug}"



class Seat(models.Model):
    show = models.ForeignKey(Show, on_delete=models.CASCADE, null=True)
    state = models.IntegerField(choices=SEAT_STATES, default=1)
    slug = AutoSlugField(populate_from=[str('seat')], db_index=True,
                        unique=True, slugify_function=append_slug)
    
    def __str__(self):
        return f"{self.slug}"


class Ticket(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    seat = models.ForeignKey(Seat, on_delete=models.CASCADE, null=True)
    price = models.PositiveIntegerField(default=20, validators=[MaxValueValidator(100)])
    slug = AutoSlugField(populate_from=[str('ticket')], db_index=True,
                        unique=True, slugify_function=append_slug)

    def __str__(self):
        return f"{self.slug}"
