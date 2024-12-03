from rest_framework import serializers
from food.serializers import FoodSerializer
from food_category.models import FoodCategory


class FoodListSerializer(serializers.ModelSerializer):
    foods = FoodSerializer(source='food', many=True, read_only=True)

    class Meta:
        model = FoodCategory
        fields = ('id', 'name_ru', 'name_en', 'name_ch', 'order_id', 'foods')
        