from django.shortcuts import render, redirect
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView,
)
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from .models import Post


class PostListView(ListView):
    model = Post
    template_name = "blog/home.html"
    context_object_name = "posts"
    ordering = ["-date_posted"]

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["sidebar_posts"] = Post.objects.all().order_by("last_modified")
        context["title"] = "Home"
        return context


class PostDetailView(DetailView):
    model = Post


class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    template_name = "blog/post_form.html"
    fields = ["title", "content"]

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    template_name = "blog/post_form.html"
    fields = ["title", "content"]

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False

    def handle_no_permission(self):
        return redirect("blog-home")


class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post


def about(request):
    context = {"title": "About"}
    return render(request, template_name="blog/about.html", context=context)
