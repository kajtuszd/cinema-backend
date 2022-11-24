from django.urls import path
from .views import UserListView

urlpatterns = [
    path('users/', UserListView.as_view(), name='user_list_view'),
    # path('users/<slug>', ModeratorView.as_view(), name='user_detail_view'),
]
