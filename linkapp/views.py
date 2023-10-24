from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView

from .models import Profile, Link

# Create your views here.


class LinkListView(ListView):
    model = Link
    # template called model_list.html -> link_list.html


class LinkCreateView(CreateView):
    # create forms.py file & form
    # check if this was a post or get request
    # return an empty form or  save the form data
    model = Link
    fields = "__all__"
    success_url = reverse_lazy("link-list")
    # template called model_form.html -> link_form.html
