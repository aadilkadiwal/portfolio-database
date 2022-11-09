from django.contrib import admin

from .models import (
    About,
    Bio,
    Language,
    Skill,
    Project,
    Experience,
    Education
)


@admin.register(About)
class AboutAdmin(admin.ModelAdmin):
    list_display = [field.name for field in About._meta.fields]


@admin.register(Bio)
class BioAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Bio._meta.fields]


@admin.register(Language)
class LanguageAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Language._meta.fields]
    list_filter = ["rating",]


@admin.register(Skill)
class SkillAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Skill._meta.fields]
    list_filter = ["skill_type", "status",]
    search_fields = ["name",]


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Project._meta.fields]
    search_fields = ["name",]


@admin.register(Experience)
class ExperienceAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Experience._meta.fields]
    search_fields = ["company_name",]


@admin.register(Education)
class EducationAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Education._meta.fields]