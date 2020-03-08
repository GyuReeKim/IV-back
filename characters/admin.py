from django.contrib import admin
from .models import Character, Position, Persona, Trait, Survivor, Hunter

# Register your models here.
admin.site.register(Character)
admin.site.register(Position)
admin.site.register(Persona)
admin.site.register(Trait)
admin.site.register(Survivor)
admin.site.register(Hunter)
