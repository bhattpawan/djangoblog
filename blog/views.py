from typing import Any
from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Post


def home(request):
    posts = Post.objects.all()
    context = {
        "posts": posts,
        "title": "Home",
        "sidebar_posts": posts.order_by("-last_modified"),
    }
    return render(request, template_name="blog/home.html", context=context)


class PostListView(ListView):
    model = Post
    template_name = "blog/home.html"
    context_object_name = "posts"
    ordering = ["-date_posted"]

    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context["sidebar_posts"] = Post.objects.all().order_by("-last_modified")
        context["title"] = "Home"
        return context


class PostDetailView(DetailView):
    model = Post

    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context["sidebar_posts"] = Post.objects.all().order_by("-last_modified")
        context["title"] = "Home"
        return context


def about(request):
    context = {"title": "About"}
    return render(request, template_name="blog/about.html", context=context)
