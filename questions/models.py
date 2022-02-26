from django.db import models

from django.urls import reverse
from django.template.defaultfilters import slugify

from users.models import *
from helpers.models import *


class Tag(TrackingModel):
    name = models.CharField(max_length=70, null=True)

    def __str__(self):
        return self.name

class Question(TrackingModel):
    questioner = models.ForeignKey(UserProfile, on_delete=models.DO_NOTHING)
    title = models.CharField(max_length=200, null=True)
    slug = models.SlugField(unique=True)
    tag = models.ForeignKey(Tag, on_delete=models.SET_NULL, null=True)
    question = models.TextField()
    date_asked = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return f'{self.title}'

    def get_absolute_url(self):
        return reverse('questions:question', kwargs={'slug': self.slug})

    def save(self, *args, **kwargs): 
        if not self.slug:
            self.slug = slugify(self.title)
        return super().save(*args, **kwargs)

class Answer(TrackingModel):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    answerer = models.ForeignKey(UserProfile, on_delete=models.DO_NOTHING)
    answer = models.TextField()

    def __str__(self):
        return f'{self.question.title}'


# ToDo: Modify this model and create a default userprofile and tag so that once someone deletes their profile, the default userprofile would claim the question. 