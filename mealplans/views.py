from django.shortcuts import redirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.views.generic.list import ListView

from mealplans.models import Mealplan


class MealPlanListView(ListView):
    model = Mealplan
    template_name = "mealplans/list.html"
    paginate_by = 2


class MealPlanDetailView(DetailView):
    model = Mealplan
    template_name = "mealplans/detail.html"


class MealPlanCreateView(CreateView):
    model = Mealplan
    template_name = "mealplans/new.html"
    fields = ["name"]
    success_url = reverse_lazy("tags_list")


class MealPlanUpdateView(UpdateView):
    model = Mealplan
    template_name = "mealplans/edit.html"
    fields = ["name"]
    success_url = reverse_lazy("tags_list")


class MealPlanDeleteView(DeleteView):
    model = Mealplan
    template_name = "mealplans/delete.html"
    success_url = reverse_lazy("tags_list")
