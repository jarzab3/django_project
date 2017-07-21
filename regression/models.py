from django.db import models
from regression.choices import *


class UserStory(models.Model):
    # case_title = models.CharField(max_length=200)
    case_title = models.IntegerField(choices=SUBJECT_CHOICES, default=1)
    subject = models.CharField(max_length=200)
    test_preconditions = models.CharField(max_length=200, null=True, blank=True)
    repro_steps = models.CharField(max_length=200, null=True, blank=True)
    extra_notes = models.CharField(max_length=200, null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)

class EmailCategory(models.Model):
    key = models.CharField(max_length=200)

