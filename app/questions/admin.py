from django.contrib import admin
from questions.models import Question, Comment


class CommentInline(admin.StackedInline): #structure of runserver admin page
    model = Comment
    extra = 3
    #Comment boxes

class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,               {'fields': ['question_text']}),
    
    ]
    inlines = [CommentInline]
    #I added questions onto server admin page

admin.site.register(Question, QuestionAdmin) #per polls app tutorial
#Custom code makes this viewable on the admin page (runserver)




