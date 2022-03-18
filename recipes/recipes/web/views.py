from django.shortcuts import render, redirect
from django.urls import reverse_lazy, reverse
from django.views.generic import CreateView

from recipes.web.forms import CreateRecipeForm, EditRecipeForm, DeleteRecipeForm
from recipes.web.models import Recipe


def get_recipes():
    recipes = Recipe.objects.all()
    recipes_list = [r.title for r in recipes]
    if len(recipes_list) > 0:
        return True

    return False


def show_index(request):
    recipe = get_recipes()
    recipes = Recipe.objects.all()

    context = {
        'recipe': recipe,
        'recipes': recipes,
    }

    return render(request, 'index.html', context)


# def create_recipe(request):
#     if request.method == 'POST':
#         form = CreateRecipeForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('show index')
#     else:
#         form = CreateRecipeForm()
#     context = {
#         'form': form,
#     }
#     return render(request, 'create.html', context)

class RecipeCreateView(CreateView):
    model = Recipe
    template_name = 'create.html'
    success_url = reverse_lazy('show index')
    fields = '__all__'


def edit_recipe(request, pk):
    recipe = Recipe.objects.get(pk=pk)
    if request.method == 'POST':
        form = EditRecipeForm(request.POST, instance=recipe)
        if form.is_valid():
            form.save()
            return redirect('show index')
    else:
        form = EditRecipeForm(instance=recipe)
    context = {
        'form': form,
        "recipe": recipe,
    }
    return render(request, 'edit.html', context)


def delete_recipe(request, pk):
    recipe = Recipe.objects.get(pk=pk)
    if request.method == 'POST':
        Recipe.delete(recipe)
        return redirect('show index')
    else:
        form = DeleteRecipeForm(instance=recipe)
        context = {
            'form': form,
            "recipe": recipe,
        }
    return render(request, 'delete.html', context)


def recipe_details(request, pk):
    recipe = Recipe.objects.get(pk=pk)
    ingredients = recipe.ingredients
    list_ingredients = ingredients.split(", ")
    context = {
        'recipe': recipe,
        'list_ingredients': list_ingredients,
    }
    return render(request, 'details.html', context)
