from django.shortcuts import render, HttpResponse


recipes = [
    {
    'author': 'James',
    'title': 'Meatball Sub',
    'Directions': 'Combine all Ingredients',
    'date_posted': 'July 1st, 2024'
    },
    {
    'author': 'James',
    'title': 'Turkey Sub',
    'Directions': 'Combine all Ingredients',
    'date_posted': 'July 3rd, 2024'
    },
    {
    'author': 'James',
    'title': 'Ham/Cheese Sub',
    'Directions': 'Combine all Ingredients',
    'date_posted': 'July 7th, 2024'
    },
    ]
# Create your views here.
def Home(request):
    context = {
        'recipes': recipes
    }
    return render(request, "recipes/home.html", context) 

def About(request):
    return render(request, "recipes/about.html", {'title': 'About us'})