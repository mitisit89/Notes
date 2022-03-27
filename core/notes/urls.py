from django.urls import path
from . import views


urlpatterns = [
    path("", views.IndexView.as_view(), name="index"),
    path("create", views.CreateNoteView.as_view(), name="create_note"),
]
