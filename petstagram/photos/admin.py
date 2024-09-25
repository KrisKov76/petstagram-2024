from django.contrib import admin

from petstagram.photos.models import Photo


@admin.register(Photo)
class Admin(admin.ModelAdmin):
    pass
    

# Register your models here.
