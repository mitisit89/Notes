from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect


def sing_in(response):
    if response.method == "POST":
        form = UserCreationForm(response.POST)
        if form.is_valid:
            form.save()
        return redirect("/notes")
    else:
        form = UserCreationForm()
    return render(response, "signin.html", {"form": form})
