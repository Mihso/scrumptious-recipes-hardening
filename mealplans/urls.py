from django.urls import path


from mealplans.views import (
    MealPlanListView,
    MealPlanCreateView,
    MealPlanDetailView,
    MealPlanDeleteView,
    MealPlanUpdateView,
)

urlpatterns = [
    path("", MealPlanListView.as_view(), name="mealplans_list"),
    path("<int:pk>/", MealPlanDetailView.as_view(), name="mealplan_detail"),
    path(
        "<int:pk>/delete/", MealPlanDeleteView.as_view(), name="mealplan_delete"
    ),
    path("new/", MealPlanCreateView.as_view(), name="mealplan_new"),
    path("<int:pk>/edit/", MealPlanUpdateView.as_view(), name="mealplan_edit"),
]
