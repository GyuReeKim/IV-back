from rest_framework import serializers
from .models import Character


class CharacterSerializer(serializers.ModelSerializer):
    image = serializers.ImageField(use_url=True, required=False)

    class Meta:
        model = Character
        fields = (
            'id', 'name', 'another_name', 
            'image', 'explanation', 'difficulty',
        )
        read_only_fields = ('id',)