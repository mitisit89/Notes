from django.urls import path
from . import views


urlpatterns = [
    path("sing_in", views.sing_in, name="sing_in"),
    path('',views.login, name="login"),
]
