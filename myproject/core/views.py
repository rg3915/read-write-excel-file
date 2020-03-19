from django.shortcuts import render
from django.urls import reverse_lazy as r
from django.views.generic import CreateView, ListView, DetailView
from django.views.generic import UpdateView, DeleteView
from .mixins import NameSearchMixin
from .models import Person
from .forms import PersonForm


def home(request):
    return render(request, 'index.html')


class PersonList(NameSearchMixin, ListView):
    model = Person
    paginate_by = 10


person_detail = DetailView.as_view(model=Person)

person_create = CreateView.as_view(model=Person, form_class=PersonForm)

person_update = UpdateView.as_view(model=Person, form_class=PersonForm)

person_delete = DeleteView.as_view(model=Person, success_url=r('core:person_list'))
