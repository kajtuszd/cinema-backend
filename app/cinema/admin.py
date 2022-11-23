from django.contrib import admin
from .models import Seat, Show, Movie, Hall, Ticket


class HallAdmin(admin.ModelAdmin):
    list_display = ('hall_number', 'seats_number',)
    ordering = ('hall_number', 'seats_number',)


class MovieAdmin(admin.ModelAdmin):
    list_display = ('title', 'production_year', 'time_in_minutes',)
    search_fields = ('title',)
    ordering = ('title', 'production_year', 'time_in_minutes',)


class ShowAdmin(admin.ModelAdmin):
    def hall_number(self, obj):
        return obj.hall.hall_number

    list_display = ('movie', 'hall_number', 'start_time',)
    search_fields = ('movie',)
    ordering = ('movie', 'start_time',)


class TicketAdmin(admin.ModelAdmin):
    def movie(self, obj):
        return obj.seat.show.movie

    list_display = ('owner', 'price', 'movie', 'slug',)
    list_filter = ('owner',)
    search_fields = ('owner', 'movie', 'slug',)
    ordering = ('owner', 'price',)


class SeatAdmin(admin.ModelAdmin):
    list_display = ('slug', 'show', 'state',)
    list_filter = ('state',)
    ordering = ('show',)


admin.site.register(Seat, SeatAdmin)
admin.site.register(Show, ShowAdmin)
admin.site.register(Movie, MovieAdmin)
admin.site.register(Hall, HallAdmin)
admin.site.register(Ticket, TicketAdmin)
