from django.contrib import admin


# Register your models here.
from tracker.models import Event, Exercise, Attribute, AttributeType

admin.site.register(Event)
admin.site.register(Exercise)
admin.site.register(Attribute)
admin.site.register(AttributeType)


