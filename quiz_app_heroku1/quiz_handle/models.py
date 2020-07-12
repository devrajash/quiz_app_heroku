from django.db import models

from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.db import models
from django.contrib.auth.models import User
from django import forms

class Post(models.Model):
    question=models.CharField(max_length=100)
    question_A=models.CharField(max_length=100,default='')
    question_B=models.CharField(max_length=100,default='')
    question_C=models.CharField(max_length=100,default='')
    question_D=models.CharField(max_length=100,default='')
    answer=models.CharField(max_length=100,default='')