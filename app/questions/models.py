from django.db import models

# Create your models here.

class Question(models.Model):
    #models = tables in database. we want fields for questions and fields
    #for comment. Think of this as Excel doc. These are headers/columns
    #hypothetical Excel spreadsheet called "Question". Column in "Question sheet called
    #question_text
    question_text = models.CharField(max_length=200)


class Comment(models.Model):
    comment_text = models.CharField(max_length=200)

    #I also need you to be able to go back and find a question for me
    #don't ask the question which comment it's related to
    #ask the comment what question
    question = models.ForeignKey(Question)
    #'question' is a field in "Comment"
