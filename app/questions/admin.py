from django.contrib import admin
from questions.models import Question, Comment
# Register your models here.


class CommentInline(admin.StackedInline): #I need to figure out why this works
    model = Comment
    extra = 3


class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,               {'fields': ['question_text']}),
    
    ]
    inlines = [CommentInline]

admin.site.register(Question, QuestionAdmin) #per polls app tutorial
#Custom code makes this viewable on the admin page (runserver)




