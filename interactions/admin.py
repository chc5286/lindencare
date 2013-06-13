from django.contrib import admin

from .models import Interaction, InteractionType


admin.site.register(Interaction)
admin.site.register(InteractionType)


