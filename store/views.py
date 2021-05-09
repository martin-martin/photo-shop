from django.shortcuts import render
from .models import Category


def home(request):
    categories = Category.objects.all()

    context = {
        "categories": categories
    }
    return render(request, 'store/home.html', context)

def categories(request):
    return render(request, 'store/categories.html')
