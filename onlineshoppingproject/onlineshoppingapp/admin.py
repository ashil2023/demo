from django.contrib import admin

# Register your models here.
from . models import place
from . models import Profile
admin.site.register(place)
admin.site.register(Profile)
