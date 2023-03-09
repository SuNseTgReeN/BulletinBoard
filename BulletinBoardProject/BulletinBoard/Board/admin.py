from django.contrib import admin
from django.contrib.auth.models import User

from .models import Category, Notification, Responses

admin.site.register(Category)
admin.site.register(Notification)
admin.site.register(Responses)

