from django.db import models


class Question(models.Model):
    question_text = models.CharField(max_length=200)
    #models = tables in database. we want fields for questions and fields
    #for comment. Think of this as Excel doc. These are headers/columns
    #hypothetical Excel spreadsheet called "Question". Column in "Question" sheet
    #called question_text


class Comment(models.Model):
    comment_text = models.CharField(max_length=200)
    question = models.ForeignKey(Question) #many-to-one relationship
    
#go back and find a question.
#Don't ask the question which comment it's related to, ask the comment to what question it belongs.
#'question' is a field in "Comment"
