from django.contrib import admin
from .models import TelegramUser
from .models import UserProfile

admin.site.register(TelegramUser)
admin.site.register(UserProfile)
