from django.db import models

from core.models import AbstractTrack


class About(AbstractTrack):
    description = models.CharField(max_length=255, null=True, blank=True)


class Bio(AbstractTrack):
    dob = models.DateField()
    email = models.EmailField()
    city = models.CharField(max_length=30)

    def __str__(self):
        return f"{self.dob} | {self.email} | {self.city}"


class Language(AbstractTrack):
    class Rating(models.TextChoices):
        STAR_1 = "STAR_1"
        STAR_2 = "STAR_2"
        STAR_3 = "STAR_3"
        STAR_4 = "STAR_4"
        STAR_5 = "STAR_5"

    name = models.CharField(max_length=20)
    rating = models.CharField(choices=Rating.choices, default=Rating.STAR_1, max_length=6)

    def __str__(self):
        return f"{self.name} | {self.rating}"


class Skill(AbstractTrack):
    class SkillType(models.TextChoices):
        PROFESSIONAL_SKILL = 'PROFESSIONAL_SKILL'
        SOFTWARE_SKILL = 'SOFTWARE_SKILL'
        CODE_SKILL = 'CODE_SKILL'

    class Status(models.TextChoices):
        BEGINNER = 'BEGINNER'
        INTERMEDIATE = 'INTERMEDIATE'
        ADVANCE = 'ADVANCE'
        EXPERT = 'EXPERT'

    name = models.CharField(max_length=55)
    skill_type = models.CharField(choices=SkillType.choices, default=SkillType.CODE_SKILL, max_length=18)
    status = models.CharField(choices=Status.choices, default=Status.BEGINNER, max_length=12)

    def __str__(self):
        return f"{self.name} | {self.status}"

    
class Project(AbstractTrack):
    name = models.CharField(max_length=55)
    description = models.CharField(max_length=155)
    image = models.ImageField(upload_to='project/')
    url = models.URLField()

    def __str__(self):
        return f"{self.name} | {self.url}"


class Experience(AbstractTrack):
    company_name = models.CharField(max_length=55)
    designation = models.CharField(max_length=55)
    description = models.CharField(max_length=255)
    start_date = models.DateField()
    end_date = models.DateField()

    def __str__(self):
        return f"{self.company_name} | {self.designation}"


class Education(AbstractTrack):
    degree = models.CharField(max_length=100)
    course_name = models.CharField(max_length=155)
    university = models.CharField(max_length=155)
    start_date = models.DateField()
    end_date = models.DateField()

    def __str__(self):
        return f"{self.degree} | {self.course_name}"