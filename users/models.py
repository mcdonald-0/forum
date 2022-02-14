from django.db import models

from authentication.models import *


def get_image_filepath(self, *args, **kwargs):
	return f"profile_images/{self.pk}/{'profile_image.png'}"

def get_default_image():
	return 'icons/male.png'

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_image  = models.ImageField(max_length=255, upload_to=get_image_filepath, null=True, blank=True, default=get_default_image)
    first_name = models.CharField(max_length=150, null=True)
    last_name = models.CharField(max_length=150, null=True)
    birthdate = models.DateField(null=True)
    GENDER_CHOICES = (
    		('M', 'Male'),
    		('F', 'Female'),
    	)
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES, null=True)
    bio = models.TextField(null=True, blank=True)
    date_of_profile_update = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return '%s %s' % (self.first_name, self.last_name)


