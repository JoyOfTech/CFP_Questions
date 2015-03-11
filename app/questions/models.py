from django.db import models


class Question(models.Model):
    #models = tables in database. we want fields for questions and fields
    #for comment. Think of this as Excel doc. These are headers/columns
    #hypothetical Excel spreadsheet called "Question". Column in "Question sheet
    #called question_text
    question_text = models.CharField(max_length=200)


class Comment(models.Model):
    comment_text = models.CharField(max_length=200)

    #go back and find a question.
    #Don't ask the question which comment it's related to
    #ask the comment to what question it belongs
    question = models.ForeignKey(Question)
    #'question' is a field in "Comment"
