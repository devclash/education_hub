from django.shortcuts import render
from django.views.generic import ListView, CreateView
from .models import Question
# Create your views here.
# This is the view for index/home page of education hub


class QuestionListView(ListView):
    '''
    List View for Question Template
    '''
    model = Question
    template_name = 'index.html'
    context_object_name = 'questions'


class QuestionCreateView(CreateView):
    '''
    Create View for Question model
    '''
    model = Question
    fields = ['title', 'description']
