import os
from django.db import models
from django.conf import settings
from django.core.files.storage import FileSystemStorage

# Create your models here.

# 이미지 덮어쓰기
class OverwriteStorage(FileSystemStorage):
    def get_available_name(self, name, max_length=None):
        if self.exists(name):
            os.remove(os.path.join(settings.MEDIA_ROOT, name))
        return name


class Character(models.Model):
    name = models.CharField(max_length=50)
    another_name = models.CharField(max_length=50)
    image = models.ImageField(upload_to="character", null=True, blank=True, storage=OverwriteStorage())
    explanation = models.TextField()
    difficulty = models.CharField(max_length=50, null=True, blank=True) # 난이도 # 컨트롤 난이도가 높습니다.
    
    def __str__(self):
        return f'{self.name} ({self.another_name})'


class Position(models.Model):
    position_name = models.CharField(max_length=50)
    position_grade = models.CharField(max_length=50)
    position_role = models.TextField()

    def __str__(self):
        return f'{self.position_name} - {self.position_grade}'


class Persona(models.Model):
    persona_sort = models.CharField(max_length=50)
    persona_name = models.CharField(max_length=50)
    persona_direction = models.IntegerField() # 몇시 인격
    persona_parent = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True)
    persona_point = models.IntegerField()
    persona_explanation = models.TextField()
    persona_opinion = models.TextField(null=True, blank=True) # 인격에 대한 의견 (사용할 지 고민)

    def __str__(self):
        return f'{self.persona_name} - {self.persona_point}'


class Trait(models.Model):
    trait_name = models.CharField(max_length=50)
    trait_cooldown = models.IntegerField(null=True, blank=True)
    trait_explanation = models.CharField(max_length=50)
    trait_opinion = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.trait_name


class Survivor(models.Model):
    character = models.ForeignKey(Character, on_delete=models.CASCADE)
    positions_of_survivor = models.ManyToManyField(Position, related_name="survivors_of_positon")
    position_explanation = models.TextField(null=True, blank=True)
    external_trait1 = models.CharField(max_length=50)
    external_trait1_explanation = models.TextField()
    external_trait2 = models.CharField(max_length=50, null=True, blank=True)
    external_trait2_explanation = models.TextField(null=True, blank=True)
    external_trait3 = models.CharField(max_length=50, null=True, blank=True)
    external_trait3_explanation = models.TextField(null=True, blank=True)
    external_trait4 = models.CharField(max_length=50, null=True, blank=True)
    external_trait4_explanation = models.TextField(null=True, blank=True)
    rumor = models.TextField()
    suitable_personas_of_survivor = models.ManyToManyField(Persona, related_name="suitable_survivors_of_persona")
    persona_build_explanation = models.TextField(null=True, blank=True)

    def __str__(self):
        return f'{self.character.another_name} (생존자)'


class Hunter(models.Model):
    character = models.ForeignKey(Character, on_delete=models.CASCADE)
    positions_of_hunter = models.ManyToManyField(Position, related_name="hunters_of_position")
    position_explanation = models.TextField(null=True, blank=True)
    external_trait1 = models.CharField(max_length=50)
    external_trait1_explanation = models.TextField()
    external_trait2 = models.CharField(max_length=50, null=True, blank=True)
    external_trait2_explanation = models.TextField(null=True, blank=True)
    external_trait3 = models.CharField(max_length=50, null=True, blank=True)
    external_trait3_explanation = models.TextField(null=True, blank=True)
    external_trait4 = models.CharField(max_length=50, null=True, blank=True)
    external_trait4_explanation = models.TextField(null=True, blank=True)
    rumor = models.TextField()
    suitable_personas_of_hunter = models.ManyToManyField(Persona, related_name="suitable_hunters_of_persona")
    persona_build_explanation = models.TextField(null=True, blank=True)
    suitable_traits_of_hunter = models.ManyToManyField(Trait, related_name="suitable_hunters_of_trait")
    trait_recommendation = models.TextField(null=True, blank=True)
    shapeshift1 = models.CharField(max_length=50, null=True, blank=True)
    shapeshift1_explanation = models.TextField(null=True, blank=True)
    shapeshift1_sub = models.CharField(max_length=50, null=True, blank=True)
    shapeshift1_sub_explanation = models.TextField(null=True, blank=True)
    shapeshift2 = models.CharField(max_length=50)
    shapeshift2_explanation = models.TextField()
    shapeshift2_sub = models.CharField(max_length=50, null=True, blank=True)
    shapeshift2_sub_explanation = models.TextField(null=True, blank=True)
    shapeshift3 = models.CharField(max_length=50)
    shapeshift3_explanation = models.TextField()
    shapeshift3_sub = models.CharField(max_length=50, null=True, blank=True)
    shapeshift3_sub_explanation = models.TextField(null=True, blank=True)

    def __str__(self):
        return f'{self.character.another_name} (감시자)'


# class Skin(models.Model):
#     character = models.ForeignKey(Character, on_delete=models.CASCADE)
#     skin_name = models.CharField(max_length=50)
#     skin_explanation = models.TextField()
#     # skin_image = models.ImageField()


# class Accessory(models.Model):
    # skin은 manytomany로 바꾸자
#     skin = models.ForeignKey(Skin, on_delete=models.CASCADE)
#     accessory_name = models.CharField(max_length=50)
#     accessory_explanation = models.TextField()
#     # accessory_image = models.ImageField()


# class Survey(models.Model):
#     survey_keyword = models.CharField(max_length=50)
#     survey_content = models.TextField()


# class Answer(models.Model):
#     survey = models.ForeignKey(Survey, on_delete=models.CASCADE)
#     answer_content = models.TextField()
#     character_list = models.ManyToManyField(Character, related_name="answer_list")


# class Recommendation(models.Model):
#     user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
#     character = models.ForeignKey(Character, on_delete=models.CASCADE)
#     created_at = models.DateTimeField(auto_now_add=True)
