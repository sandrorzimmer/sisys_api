from django.contrib import admin

from sisys_api import models

admin.site.register(models.UserProfile)
admin.site.register(models.Tag)
admin.site.register(models.Info)
