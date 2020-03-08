from rest_framework import serializers
from .models import Character, Position, Persona, Trait, Survivor
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


class PersonaChildSerializer(serializers.ModelSerializer):
    class Meta:
        model = Persona
        fields = (
            'id', 'persona_sort', 
            'persona_name', 'persona_direction', 
            'persona_point', 'persona_explanation', 'persona_opinion',
        )
        read_only_fields = ('id',)


class TraitSerializer(serializers.ModelSerializer):
    class Meta:
        model = Trait
        fields = '__all__'
        # fields = (
        #     'id', 'trait_name', 'trait_cooldown', 
        #     'trait_explanation', 'trait_opinion',
        # )
        read_only_fields = ('id',)


class SurvivorSerializer(serializers.ModelSerializer):
    character = CharacterSerializer()

    class Meta:
        model = Survivor
        fields = (
            'id', 'character', 'position_explanation', 
            'external_trait1', 'external_trait1_explanation', 
            'external_trait2', 'external_trait2_explanation', 
            'external_trait3', 'external_trait3_explanation', 
            'external_trait4', 'external_trait4_explanation', 
            'rumor', 'persona_build_explanation',
        )
        read_only_fields = ('id',)


class SurvivorSetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Survivor
        fields = (
            'id', 'position_explanation', 
            'external_trait1', 'external_trait1_explanation', 
            'external_trait2', 'external_trait2_explanation', 
            'external_trait3', 'external_trait3_explanation', 
            'external_trait4', 'external_trait4_explanation', 
            'rumor', 'persona_build_explanation',
        )
        read_only_fields = ('id',)
