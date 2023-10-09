from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import UserRegisterForm


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
def profile(request):
    return render(request, "users/profile.html")
