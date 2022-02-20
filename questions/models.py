from operator import mod
from django.db import models

from users.models import *
from helpers.models import *


class Tag(TrackingModel):
    name = models.CharField(max_length=70, null=True)

    def __str__(self):
        return self.name

class Question(TrackingModel):
    questioner = models.ForeignKey(UserProfile, on_delete=models.DO_NOTHING)
    tag = models.ForeignKey(Tag, on_delete=models.SET_NULL, null=True)
    title = models.CharField(max_length=2000, null=True)
    question = models.TextField()
    date_asked = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return f'\"{self.question}"'

class Answer(TrackingModel):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    answerer = models.OneToOneField(UserProfile, on_delete=models.DO_NOTHING)
    answer = models.TextField()

    def __str__(self):
        return f'{self.answerer}\'s answer to the question {self.question}'


# ToDo: Modify this model and create a default userprofile and tag so that once someone deletes their profile, the default userprofile would claim the question. 