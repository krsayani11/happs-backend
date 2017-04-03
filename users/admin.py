from django.contrib import admin
from .models import User, Friends

# Register your models here.
admin.site.register(User)
admin.site.register(Friends)