from django.contrib import admin

from .models import (
    Language,
    Skill,
    Project,
    Experience,
    Education
)


@admin.register(Language)
class LanguageAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Language._meta.fields]
    list_filter = ["rating", "is_active",]


@admin.register(Skill)
class SkillAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Skill._meta.fields]
    list_filter = ["skill_type", "is_active",]
    search_fields = ["name",]


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Project._meta.fields]
    list_filter = ["is_active",]
    search_fields = ["name",]


@admin.register(Experience)
class ExperienceAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Experience._meta.fields]
    list_filter = ["is_active",]
    search_fields = ["company_name",]


@admin.register(Education)
class EducationAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Education._meta.fields]
    list_filter = ["is_active",]