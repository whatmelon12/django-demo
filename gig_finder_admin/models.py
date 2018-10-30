from django.db import models

class Job(models.Model):
	title = models.CharField(max_length=250, default='')
	link = models.CharField(max_length=250, default='')
	category = models.CharField(max_length=250, default='')

class Ints(models.Model):
	ints1 = models.CharField(max_length=250, default='')
	ints2 = models.CharField(max_length=250, default='')

class User(models.Model):
	FirstName = models.CharField(max_length=250, default='')
	LastName = models.CharField(max_length=250, default='')
	Email = models.CharField(max_length=250, default='')
	interest1 = models.CharField(max_length=250, default='')
	interest2 = models.CharField(max_length=250, default='')