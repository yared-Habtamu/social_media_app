from django.urls import path
from .views import (
    UserRegistrationView,
    UserLoginView,
    UserLogoutView,
    UserProfileView,
    FollowUserView,
    UnfollowUserView,
    UserListView,
)

urlpatterns = [
    path('auth/register/', UserRegistrationView.as_view(), name='register'),
    path('auth/login/', UserLoginView.as_view(), name='login'),
    path('auth/logout/', UserLogoutView.as_view(), name='logout'),
    path('users/', UserListView.as_view(), name='user-list'),
    path('<int:user_id>/', UserProfileView.as_view(), name='user-profile'),
    path('<int:user_id>/follow/', FollowUserView.as_view(), name='follow-user'),
    path('<int:user_id>/unfollow/', UnfollowUserView.as_view(), name='unfollow-user'),
]