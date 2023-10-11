from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import UserRegisterForm, UserUpdateForm, ProfileUpdateForm
from blog.models import Post
from django.contrib.auth.models import User


def register(request):
    if request.user.is_authenticated:
        return redirect("blog-home")
    form = UserRegisterForm()
    if request.method == "POST":
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get("username")
            messages.success(request, f"Account Created for {username}")
            form.save()
            return redirect("login_user")
    context = {"form": form}
    return render(request, "users/register.html", context=context)


@login_required()
def profile(request, pk):
    user = User.objects.get(id=pk)
    if str(pk) == str(request.user.id):
        userUpdateForm = UserUpdateForm(instance=request.user)
        profileUpdateForm = ProfileUpdateForm(instance=request.user.profile)
        posts = Post.objects.filter(author=request.user)
        if request.method == "POST":
            userUpdateForm = UserUpdateForm(request.POST, instance=request.user)
            profileUpdateForm = ProfileUpdateForm(
                request.POST, request.FILES, instance=request.user.profile
            )
            if userUpdateForm.is_valid() and profileUpdateForm.is_valid():
                userUpdateForm.save()
                profileUpdateForm.save()
                messages.success(request, "Profile Updated Successfully")
                redirect("user_profile")
    else:
        userUpdateForm = None
        profileUpdateForm = None
        posts = Post.objects.filter(author=pk)

    context = {
        "userUpdateForm": userUpdateForm,
        "profileUpdateForm": profileUpdateForm,
        "sidebar_posts": posts,
        "user": user,
    }
    return render(request, "users/profile.html", context=context)
