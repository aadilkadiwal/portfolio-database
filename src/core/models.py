from django.db import models
from uuid import uuid4


class AbstractTrack(models.Model):
    uuid = models.UUIDField(unique=True, default=uuid4, editable=False)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class AbstractActiveTrack(AbstractTrack):
    is_active = models.BooleanField(default=True)

    class Meta:
        abstract = True


class User(AbstractTrack):
    first_name = models.CharField(max_length=55)
    surname = models.CharField(max_length=55)
    designation = models.CharField(max_length=55, null=True, blank=True)
    photo = models.ImageField(upload_to="profile/", null=True, blank=True)
    background_image = models.ImageField(upload_to="background/", null=True, blank=True)

    def __str__(self):
        return f"{self.first_name} | {self.surname}" 


class About(AbstractTrack):
    description = models.CharField(max_length=255, null=True, blank=True)


class Bio(AbstractTrack):
    dob = models.DateField()
    email = models.EmailField()
    city = models.CharField(max_length=30)

    def __str__(self):
        return f"{self.dob} | {self.email} | {self.city}"