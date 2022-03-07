from django.urls import path

from recipes.web import views
from recipes.web.views import show_index, edit_recipe, delete_recipe, recipe_details, RecipeCreateView

urlpatterns = (
    path('', show_index, name='show index'),
    path('create/', views.RecipeCreateView.as_view(), name='create recipe'),
    path('edit/<int:pk>', edit_recipe, name='edit recipe'),
    path('delete/<int:pk>', delete_recipe, name='delete recipe'),
    path('details/<int:pk>', recipe_details, name='details'),


)