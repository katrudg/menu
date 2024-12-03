from django.shortcuts import render
from food_category.models import FoodCategory
from food_category.serializers import FoodListSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status


class FoodCategoryListView(APIView):
    def get(self, request, *args, **kwargs):


        categories = FoodCategory.objects.prefetch_related('food').filter(food__is_publish=True).distinct()

        serializer = FoodListSerializer(categories, many=True)
        

        return Response(serializer.data, status=status.HTTP_200_OK)
    