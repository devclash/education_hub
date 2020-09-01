from django.urls import path
from .views import (QuestionListView, QuestionCreateView,
                    QuestionDetailView, QuestionUpdateView, QuestionDeleteView)

urlpatterns = [
    path('', QuestionListView.as_view(), name='question_list'),
    path('question/create/', QuestionCreateView.as_view(), name='question_create'),
    path('question/<int:pk>/', QuestionDetailView.as_view(), name='question_detail'),
    path('question/<int:pk>/update/',
         QuestionUpdateView.as_view(), name='question_update'),
    path('question/<int:pk>/delete/',
         QuestionDeleteView.as_view(), name='question_delete'),
]
