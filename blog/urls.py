from django.urls import path
from . import views
from rest_framework.authtoken.views import obtain_auth_token




urlpatterns = [
    path('posts/', views.PostListAPIView.as_view(), name='post-list'),
    path('posts/<int:id>/', views.PostDetailAPIView.as_view(), name='post-detail'),
    path('comments/', views.CommentListAPIView.as_view(), name='comment-list'),
    path('comments/<int:id>/', views.CommentDetailAPIView.as_view(), name='comment-detail'),
    path('registration/', obtain_auth_token, name='registration'),

]


