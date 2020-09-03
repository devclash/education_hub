from django.db import models
from ckeditor.fields import RichTextField
from django.contrib.auth.models import User
from django.utils import timezone

class Event(models.Model): 
    name =  models.CharField(max_length=100)
    description = RichTextField(blank=True,null=True)
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
    author = models.ForeignKey(User,on_delete=models.CASCADE)
    timestamp = models.DateTimeField(default=timezone.now)


    def __str__(self): 
        return self.name