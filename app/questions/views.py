
from django.http import HttpResponse
#I don't think I need this because of "render()"

from django.shortcuts import render
#render(request, template_name[, dictionary][, context_instance][, content_type][, status][, current_app][, dirs])[source]
#Combines a given template with a given context dictionary and returns an HttpResponse object with that rendered text.

from questions.models import Question

#the code below is from the index/detail portion of the polls app
def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    template = loader.get_template('questions/index.html')
    context = RequestContext(request, {
        'latest_question_list': latest_question_list,
    })
    return HttpResponse(template.render(context))

#the code below is from https://github.com/franciskung/leadnow/blob/master/reports/views.py
def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    context = {'latest_question_list': latest_question_list}
    return render(request, 'questions/index.html', context)

from django.contrib import messages #will this help with the "comments" page?
from questions.models import Comment

def home(request):
    return render(request, 'home.html', {})

# Display a list of saved queries, plus an area to enter a new  query  
def query(request):
    comments  = Comment.objects.all()
    queries = Query.objects.all()
  
    return render(request, 'query.html', {'queries': queries,
                                         'comments': comments,
                                          
                                        })

# When we have saved queries, this will let you see the details of a saved query
def query_details(request, query_id):
    return render(request, 'query.html', {})

