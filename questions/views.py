from django.shortcuts import render
from django.views.generic import ListView, CreateView, DetailView
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
    # orderin


class QuestionCreateView(CreateView):
    '''
    Create View for Question model
    '''
    model = Question
    fields = ['title', 'description']

    # Setting the author befor the question is posted

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class QuestionDetailView(DetailView):
    model = Question
