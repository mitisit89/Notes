from django.shortcuts import HttpResponse


def index(req):
    return HttpResponse("Hello ,world ,this isn apps")
