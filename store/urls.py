from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name="home"),
    path('categories/<category_id>', views.categories, name="categories"),
]
