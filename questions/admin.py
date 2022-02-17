from django.contrib import admin

from questions.models import *

admin.site.register(Tag)
admin.site.register(Question)
admin.site.register(Answer)



