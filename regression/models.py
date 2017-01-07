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


class Post(models.Model):
	title = models.CharField(max_length=100)
	content = models.TextField()


	# def __unicode__(self):
	# 	return self.title

	# def __str__(self):
	# 	return self.title

	# def get_absolute_url(self):
	# 	return reverse("posts:detail", kwargs={"id": seld.id})