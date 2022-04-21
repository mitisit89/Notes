from django.urls import path
from . import views


urlpatterns = [
    path("", views.IndexView.as_view(), name="index"),
    path("create", views.CreateNoteView.as_view(), name="create_note"),
    path("update/<str:slug>", views.UpdateNoteView.as_view(), name="update_note"),
    path("delete/<str:slug>", views.DeleteNoteView.as_view(), name="delete_note"),
]
