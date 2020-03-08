from rest_framework import serializers
from .models import Character, Position


class CharacterSerializer(serializers.ModelSerializer):
    image = serializers.ImageField(use_url=True, required=False)

    class Meta:
        model = Character
        fields = (
            'id', 'name', 'another_name', 
            'image', 'explanation', 'difficulty',
        )
        read_only_fields = ('id',)


class PositionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Position
        fields = '__all__'
        # fields = (
        #     'id', 'position_name', 
        #     'position_grade', 'position_role',
        # )
        read_only_fields = ('id',)