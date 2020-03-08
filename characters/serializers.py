from rest_framework import serializers
from .models import Character, Position, Persona
from rest_framework_recursive.fields import RecursiveField


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


class PersonaSerializer(serializers.ModelSerializer):
    persona_parent = RecursiveField(required=False, allow_null=True)

    class Meta:
        model = Persona
        fields = (
            'id', 'persona_sort', 
            'persona_name', 'persona_direction', 
            'persona_parent', 'persona_point', 
            'persona_explanation', 'persona_opinion',
        )
        read_only_fields = ('id',)
