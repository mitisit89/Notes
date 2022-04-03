from django.views import generic
from django.urls import reverse_lazy
from .models import Note


class IndexView(generic.ListView):
    model = Note
    template_name = "notes/index.html"
    context_object_name = "notes_list"


class CreateNoteView(generic.CreateView):
    model = Note
    template_name = "notes/create_form.html"
    fields = ["title", "body"]
    success_url = reverse_lazy("index")
