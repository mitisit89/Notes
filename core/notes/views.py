from django.shortcuts import render, HttpResponse, get_object_or_404


def index(request) -> HttpResponse:
    return render(request, "notes/index.html")


def create_note(request) -> HttpResponse:
    return render (request, "notes/create_form.html")
