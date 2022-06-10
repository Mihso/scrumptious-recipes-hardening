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

    def get_queryset(self):
        queryset = super().get_queryset()
        print(queryset)
        return queryset


class MealPlanDetailView(LoginRequiredMixin, DetailView):
    model = Mealplan
    template_name = "mealplans/detail.html"


class MealPlanCreateView(CreateView):
    model = Mealplan
    template_name = "mealplans/new.html"
    fields = ["name", "recipes", "date"]
    success_url = reverse_lazy("mealplans_list")

    def form_valid(self, form):
        plan = form.save(commit=False)
        plan.owner = self.request.user
        plan.save()
        form.save_m2m()
        return redirect("mealplan_detail", pk=plan.id)


class MealPlanUpdateView(LoginRequiredMixin, UpdateView):
    model = Mealplan
    template_name = "mealplans/edit.html"
    fields = ["name", "recipes", "date"]
    success_url = reverse_lazy("meals_list")


class MealPlanDeleteView(LoginRequiredMixin, DeleteView):
    model = Mealplan
    template_name = "mealplans/delete.html"
    success_url = reverse_lazy("mealplans_list")
