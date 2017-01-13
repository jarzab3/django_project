from django.db import models


class UserStory(models.Model):
    subject = models.CharField(max_length=200)
    case_title = models.CharField(max_length=200)
    test_preconditions = models.CharField(max_length=200)
    repro_steps = models.CharField(max_length=200)
    extra_notes = models.CharField(max_length=200)


class EmailCategory(models.Model):
    key = models.CharField(max_length=200)


'''
class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()

    def __unicode__(self):
        return self.title

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("posts:detail", kwargs={"id": seld.id})


'''
