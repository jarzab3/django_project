import datetime
from django.db import models
from regression.choices import *
from django.contrib.auth.models import User


class Category(models.Model):
    name = models.CharField(max_length=200)
    description = models.CharField(max_length=800, null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(User)
    active = models.BooleanField(default=True)
    archived = models.BooleanField(default=False)
    last_edited = models.TimeField(default=datetime.datetime.utcnow)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ('name',)


class UserStory(models.Model):
    # category = models.ManyToManyField(choices=Category)
    category = models.ForeignKey(Category)
    subject = models.CharField(choices=SUBJECT_CHOICES, default="Default", max_length=100)
    domain = models.CharField(choices=DOMAIN_CHOICES, default="Default", max_length=100)
    case_title = models.CharField(max_length=200)
    test_preconditions = models.CharField(max_length=200, null=True, blank=True)
    repro_steps = models.CharField(max_length=400)
    extra_notes = models.CharField(max_length=400, null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(User)
    active = models.BooleanField(default=True)
    archived = models.BooleanField(default=False)
    last_edited = models.TimeField(default=datetime.datetime.utcnow)

    def __str__(self):
        return self.case_title

    class Meta:
        ordering = ('created',)

        # class EmailCategory(models.Model):
        # key = models.CharField(max_length=200)
