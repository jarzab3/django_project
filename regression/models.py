from django.db import models

class Item(models.Model):
	title = models.CharField(max_length=200)
	description = models.TextField()
	amount = models.IntegerField()

class user_story(models.Model):
	subject = models.CharField(max_length=200)
	case_title = models.TextField()
	test_preconditions = models.TextField()



class Cost(models.Model):
	cost = models.FloatField()


class Foo(models.Model):
    """A magical creature from Foo dynasty"""
    mighty_name = models.CharField(max_length=255)
    kingdoms_count = models.PositiveIntegerField(default=0)
    email = models.EmailField()  # What? Magical creatures also have emails.