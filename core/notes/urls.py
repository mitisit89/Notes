from django.urls import path
from . import views


urlpatterns = [
    path("", views.Index.as_view()),
    path("create", views.CreateNoteView.as_view(), name="create_note"),
]
