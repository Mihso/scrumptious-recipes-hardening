from webbrowser import get
from django.db import IntegrityError
from django.shortcuts import redirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.views.generic.list import ListView
from django.views.decorators.http import require_http_methods
from recipes.forms import RatingForm
from recipes.models import Ingredient, Recipe, ShoppingList


def log_rating(request, recipe_id):
    if request.method == "POST":
        form = RatingForm(request.POST)
        if form.is_valid():
            rating = form.save(commit=False)
            try:
                rating.recipe = Recipe.objects.get(pk=recipe_id)
            except Recipe.DoesNotExist:
                return redirect("recipes_list")
            rating.save()
    return redirect("recipe_detail", pk=recipe_id)


class RecipeListView(ListView):
    model = Recipe
    template_name = "recipes/list.html"
    paginate_by = 2

    def get_queryset(self):
        querystring = self.request.GET.get("q")
        if querystring == None:
            querystring = ""
        return Recipe.objects.filter(description__icontains=querystring)


class RecipeDetailView(DetailView):
    model = Recipe
    template_name = "recipes/detail.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["rating_form"] = RatingForm()
        new_list = []
        for item in self.request.user.shoppingItems.all():
            new_list.append(item.food_item)
        context["food_in_shopping_list"] = new_list
        context["servings"] = self.request.GET.get("servings")
        return context


class RecipeCreateView(LoginRequiredMixin, CreateView):
    model = Recipe
    template_name = "recipes/new.html"
    fields = ["name", "description", "image", "servings"]
    success_url = reverse_lazy("recipes_list")

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class RecipeUpdateView(LoginRequiredMixin, UpdateView):
    model = Recipe
    template_name = "recipes/edit.html"
    fields = ["name", "author", "description", "image", "servings"]
    success_url = reverse_lazy("recipes_list")


class RecipeDeleteView(LoginRequiredMixin, DeleteView):
    model = Recipe
    template_name = "recipes/delete.html"
    success_url = reverse_lazy("recipes_list")


class shoppingItemsViewList(LoginRequiredMixin, ListView):
    model = ShoppingList
    template_name = "recipes/shopping_items.html"

    def get_queryset(self):
        return ShoppingList.objects.filter(user=self.request.user)


@require_http_methods(["POST"])
def shoppingItemsCreateList(request):
    ingd = request.POST.get("ingredient_id")
    ind = Ingredient.objects.get(id=ingd)
    user = request.user
    try:
        ShoppingList.objects.create(
            user=user,
            food_item=ind.food,
        )
    except IntegrityError:
        pass
    return redirect("recipe_detail", pk=ind.recipe.id)


@require_http_methods(["POST"])
def shopppingItemsDeleteList(request):
    ShoppingList.objects.filter(user=request.user).delete()
    return redirect("recipe_shopping_items")
