from django.urls import path
from .views import PostListCreateAPIView, PostDetailAPIView, CommentListCreateAPIView, RegisterAPIView
from rest_framework.authtoken.views import obtain_auth_token



urlpatterns = [
    path('v1/posts/', PostListCreateAPIView.as_view(), name='post_list_create'),
    path('v1/posts/<int:pk>/', PostDetailAPIView.as_view(), name='post_detail'),
    path('v1/posts/<int:post_id>/comments/', CommentListCreateAPIView.as_view(), name='post_comments'),
    path('v1/registration/', RegisterAPIView.as_view(), name='registration'),

]

