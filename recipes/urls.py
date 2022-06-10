from django.urls import path

from recipes.views import (
    RecipeCreateView,
    RecipeDeleteView,
    RecipeUpdateView,
    shoppingItemsViewList,
    log_rating,
    shoppingItemsCreateList,
    shopppingItemsDeleteList,
    RecipeDetailView,
    RecipeListView,
)

urlpatterns = [
    path("", RecipeListView.as_view(), name="recipes_list"),
    path("<int:pk>/", RecipeDetailView.as_view(), name="recipe_detail"),
    path("<int:pk>/delete/", RecipeDeleteView.as_view(), name="recipe_delete"),
    path("new/", RecipeCreateView.as_view(), name="recipe_new"),
    path("<int:pk>/edit/", RecipeUpdateView.as_view(), name="recipe_edit"),
    path("<int:recipe_id>/ratings/", log_rating, name="recipe_rating"),
    path("shopping_items/", shoppingItemsViewList.as_view(), name = "recipe_shopping_items"),
    path("shopping_items/create/", shoppingItemsCreateList, name = "shopping_items_create"),
    path("shopping_items/delete/", shopppingItemsDeleteList, name = "shopping_items_delete"),
]
