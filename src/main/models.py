from django.db import models
from decimal import Decimal
from django.core.validators import MinValueValidator, MaxValueValidator

from core.models import AbstractActiveTrack


class Language(AbstractActiveTrack):

    name = models.CharField(max_length=20)
    rating = models.DecimalField(
        max_digits=3,
        decimal_places=0,
        default=Decimal(0),
        validators=[MinValueValidator(0), MaxValueValidator(100)]
    )

    def __str__(self):
        return f"{self.name} | {self.rating}"


class Skill(AbstractActiveTrack):
    class SkillType(models.TextChoices):
        PROFESSIONAL_SKILL = 'PROFESSIONAL_SKILL'
        SOFTWARE_SKILL = 'SOFTWARE_SKILL'

    name = models.CharField(max_length=55)
    skill_type = models.CharField(choices=SkillType.choices, default=SkillType.SOFTWARE_SKILL, max_length=18)

    def __str__(self):
        return f"{self.name} | {self.skill_type}"

    
class Project(AbstractActiveTrack):
    name = models.CharField(max_length=55)
    description = models.CharField(max_length=155)
    image = models.ImageField(upload_to='project/')
    url = models.URLField()

    def __str__(self):
        return f"{self.name} | {self.url}"


class Experience(AbstractActiveTrack):
    company_name = models.CharField(max_length=55)
    designation = models.CharField(max_length=55)
    description = models.CharField(max_length=255)
    start_date = models.DateField()
    end_date = models.DateField()

    def __str__(self):
        return f"{self.company_name} | {self.designation}"


class Education(AbstractActiveTrack):
    degree = models.CharField(max_length=100)
    course_name = models.CharField(max_length=155)
    university_name = models.CharField(max_length=155)
    description = models.CharField(max_length=255)
    start_date = models.DateField()
    end_date = models.DateField()

    def __str__(self):
        return f"{self.degree} | {self.course_name}"