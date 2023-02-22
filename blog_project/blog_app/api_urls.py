from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from . import api_views

urlpatterns = [
    path('posts/', api_views.PostList.as_view()),
    path('posts/<int:pk>/', api_views.PostDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)