from __future__ import unicode_literals

from django.db import models

# Create your models here.


class User(models.Model):
    name = models.CharField(max_length=100)


class Question(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    catagory = models.CharField(max_length=100)
    title = models.CharField(max_length=1000)
    desciption = models.CharField(max_length=3000)
    posted_at = models.DateTimeField(auto_now=True)


class Answer(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.CharField(max_length=2000)
    replied_at = models.DateTimeField(auto_now=True)
