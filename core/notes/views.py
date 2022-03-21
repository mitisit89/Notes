from django.views import generic
from .models import NoteForm
class Index(generic.TemplateView):
    template_name="notes/index.html"

class CreateNoteView(generic.FormView):
    template_name='notes/create_form.html'
    form_class=NoteForm
    success_url = '/notes'

