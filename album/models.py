from django.db import models

COAST_CHOICES = (
	('W', 'West Coast'), 
	('E', 'East Coast'),
	('S', 'The South'),
)

class Album(models.Model):
	name = models.CharField(max_length=200)
	slug = models.SlugField(unique=True)
	rapper = models.ForeignKey('Rapper')
	coast = models.CharField(max_length=1, choices=COAST_CHOICES)
	description = models.TextField(blank=True)
	image1 = models.ImageField(upload_to="images/albumthumbs/", blank=True)

	def __unicode__(self):
		return self.name

class Rapper(models.Model):
	name = models.CharField(max_length=200)
	slug = models.SlugField(unique=True)
	description = models.TextField(blank=True)

	def __unicode__(self):
		return self.name


