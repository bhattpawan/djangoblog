from django.urls import path
from . import views

urlpatterns = [
    path("", views.PostListView.as_view(), name="blog-home"),
    path("post/<str:pk>/", views.PostDetailView.as_view(), name="post-detail"),
    path("about/", views.about, name="blog-about"),
]
