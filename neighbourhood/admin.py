from django.contrib import admin

# Register your models here.
from .models import Neighbourhood,User,Business,Profile



admin.site.register(Neighbourhood)
admin.site.register(User)
admin.site.register(Business)
admin.site.register(Profile)
