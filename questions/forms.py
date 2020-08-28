from django import forms
from .models import Question


class QuestionForm(forms.ModelForm):
    '''
    form for the question model
    '''
    class Meta:
        model = Question
        fields = '__all__'
