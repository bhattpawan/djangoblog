from django.shortcuts import render
from .models import Post


# Create your views here.
def home(request):
    posts = Post.objects.all()
    context = {"posts": posts, "title": "Home"}
    return render(request, template_name="blog/home.html", context=context)


def about(request):
    context = {"title": "About"}
    return render(request, template_name="blog/about.html", context=context)
