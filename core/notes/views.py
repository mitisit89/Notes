from django.views import generic
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Note


class IndexView(LoginRequiredMixin, generic.ListView):
    model = Note
    login_url = "login"
    template_name = "notes/index.html"
    context_object_name = "notes_list"


class CreateNoteView(LoginRequiredMixin, generic.CreateView):
    model = Note
    login_url = "login"
    template_name = "notes/create_form.html"
    fields = [
        "title",
        "body",
    ]
    success_url = reverse_lazy("index")

    def form_valid(self, form):
        app_model = form.save(commit=False)
        app_model.created_by = self.request.user
        # app_model.user = User.objects.get(user=self.request.user) # Or explicit model 
        form.save()
        return super().form_valid(form)


class UpdateNoteView(LoginRequiredMixin, generic.UpdateView):
    model = Note
    login_url = "login"
    fields = ["title", "body"]


class DeleteNoteView(LoginRequiredMixin, generic.DeleteView):
    model = Note
    login_url = "login"
    template_name = "notes/delete.html"
    success_url = reverse_lazy("index")
