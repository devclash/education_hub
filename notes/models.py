from django.db import models
from django.utils import timezone
from ckeditor.fields import RichTextField

# Create your models here.


class Tag(models.Model):
    '''
    Model for tags that can be attached to notes
    '''
    name = models.CharField(max_length=100, null=True)

    def __str__(self):
        return self.name


class Note(models.Model):
    '''
    The actual model of our notes app
    '''
    title = models.CharField(max_length=100)
    decription = RichTextField(blank=True, null=True)
    document = models.FileField(upload_to='notes/')
    date_created = models.DateTimeField(default=timezone.now)
    tags = models.ManyToManyField(Tag)

    def __str__(self):
        return self.title
