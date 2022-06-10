Shopping List Plan

look through example to see basic functionality

Technical:

Required to be inside recipes App

4 components of shopping List
    []shopping list button next to each ingredient in any give recipes
    []a main nav link to shopping list items that includes number of items in shopping list
    []shopping list page itself with food items, individualized for user
    []a button to clear all items from shopping list

Steps:
    [x] start with making the shopping list model
        [] models.py, view.py, admin.py, urls.py
        [] model itself have two pieces of data
            [x]user, AUTH_USER_MODEL, foreign key to Django user mode, CASCADE on delete
                [x]refer to recipe model
                [x]gets user information and  links it to current shopping list
            [x]food_item, "FoodItem", foreign key to FoodItem, Protect on delete
                [x]refer to ingredient model
    [] create classes in views.py
        []shoppingItemsViewList
            []display get shopping list who's owner is the current user
                []only display shopping list of current owner
                []LoginRequireMixin
        []shoppingItemsDelete
            []remove all items in current shopping list
            []no html template
            []return to shopping list page that is empty
        []shoppingItemsCreate
            []create ShoppingItem instance in database with current user and value of submitted "ingredients_id"
            []no html template
            []return to current recipe detail page
    [] create paths in urls.py
        []/shopping_items/create
        []/shopping_items/
        []/shopping_items/delete
    []create shopping list webpage
        [x]make new html file since it needs to be in recipes app
            []include delete button that links to shoppingItemsDelete url
    [] create link to shopping list webpage
        [x] modify base.html to include link to list webpage
            [] ensure list is specific to owner
            [] include number in button with number of ingredients in shopping list
                [] | length,  get number of items in shopping list
                [] {{ length of shopping list }} 
    []add button to add ingredient to shopping list on each ingredient.
        [] modify ingredient list in detail.html
            []add button that runs shoppingItemsCreate using current ingredient_id
            []replaces button with text if item is already in shopping list
                []{% if item already in shopping cart%}
                    []{% for ingredient in shopping cart %}
                        []check if current ingredient matches with any ingredient in shopping list