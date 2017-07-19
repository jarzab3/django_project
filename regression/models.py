from django.db import models


class UserStory(models.Model):
    subject = models.CharField(max_length=200)
    case_title = models.CharField(max_length=200)
    test_preconditions = models.CharField(max_length=200)
    repro_steps = models.CharField(max_length=200)
    extra_notes = models.CharField(max_length=200)


class EmailCategory(models.Model):
    key = models.CharField(max_length=200)

