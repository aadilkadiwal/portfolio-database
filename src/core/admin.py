from django.contrib import admin
from .models import User, About, Bio


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = [field.name for field in User._meta.fields]


@admin.register(About)
class AboutAdmin(admin.ModelAdmin):
    list_display = [field.name for field in About._meta.fields]


@admin.register(Bio)
class BioAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Bio._meta.fields]