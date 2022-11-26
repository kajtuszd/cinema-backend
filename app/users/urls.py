from django.urls import path
from .views import UserListView, UserDetailView

urlpatterns = [
    path('users/', UserListView.as_view(), name='user_list_view'),
    path('users/<str:username>/', UserDetailView.as_view(), name='user_detail_view'),
]
