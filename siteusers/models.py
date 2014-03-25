from django.db import models
from django.db.models.signals import post_save
from django.contrib.auth.models import User

class SiteUser(models.Model):
	user = models.OneToOneField(User)
	birthday = models.DateField()
	name = models.CharField(max_length=100)

	def __unicode__(self):
		return self.name

# create user object to attach to SiteUser
#def create_siteuser_user_callback(sender, instance, **kwargs):
#	siteuser, new = SiteUser.objects.get_or_create(user=instance)
#post_save.connect(create_siteuser_user_callback, User)

