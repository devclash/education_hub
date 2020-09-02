from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

from questions.models import Question

# Create your models here.


class Comment(models.Model):
    author = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    # This question is not required after including the models below
    # question = models.ForeignKey(Question, on_delete=models.CASCADE)

    # Used for content types (Generic relations)
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey('content_type', 'object_id')

    comment = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return str(self.author) + ' commented '
