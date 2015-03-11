from django.contrib import admin
from questions.models import Question
# Register your models here.

admin.site.register(Question)
#Custom code makes this viewable on the admin page (runserver)
