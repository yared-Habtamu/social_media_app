from django.urls import path
from .views import (
    PostListView,
    PostDetailView,
    LikePostView,
    UnlikePostView,
    CommentListView,
    PostCreateView
)

urlpatterns = [
    path('posts/create/', PostCreateView.as_view(), name='post-create'),
    path('posts/', PostListView.as_view(), name='post-list'),
    path('posts/<int:post_id>/', PostDetailView.as_view(), name='post-detail'),
    path('posts/<int:post_id>/like/', LikePostView.as_view(), name='like-post'),
    path('posts/<int:post_id>/unlike/', UnlikePostView.as_view(), name='unlike-post'),
    path('posts/<int:post_id>/comments/', CommentListView.as_view(), name='comment-list'),
]