from django.shortcuts import render, redirect
from .forms import RegisterForm,AuthForm 


def sing_in(response):
    if response.method == "POST":
        form = RegisterForm(response.POST)
        if form.is_valid():
            form.save()
        return redirect("/notes")
    else:
        form = RegisterForm()
    return render(response, "signin.html", {"form": form})


def login(response):
    if response.method == "POST":
        form=AuthForm(response.POST)
        if form.is_valid():
            form.save()
        return redirect('/notes')
    else:
        form=AuthForm()
    return render(response,'login.html',{'form':form})
