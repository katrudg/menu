from django.urls import path
from food_category.views import FoodCategoryListView


urlpatterns = [

    path('v1/foods/', FoodCategoryListView.as_view(), name='food-category-list'),
]
