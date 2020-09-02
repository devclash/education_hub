from django.shortcuts import render
from django.views.generic import CreateView, ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin

from .models import Feedback
from django.urls import reverse
# Create your views here.


class FeedbackCreateView(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    model = Feedback
    fields = ['title', 'description']
    success_message = 'Your feedback has been successfully submitted'
    success_url = '/feedback/create/'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    # alternative to success_url

    # def get_success_url(self):
    #     return reverse('feedback_create')
