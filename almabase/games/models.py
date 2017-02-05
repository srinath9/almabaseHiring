from __future__ import unicode_literals

from django.db import models
from django_elasticsearch.models import EsIndexable

import math
# Create your models here.
from django import forms

class QueryForm(forms.Form):
    name = forms.CharField(label='name', max_length=100)
    location = forms.CharField(label='location', max_length=100)

class Games(EsIndexable, models.Model):
    title  = models.CharField(max_length=56)
    platform = models.CharField(max_length=16)
    score = models.FloatField(max_length=3)
    genre = models.CharField(max_length=17)
    editors_choice = models.CharField(max_length=1)


    def __str__(self):
        return self.title

    # def final_price(self):
    #     return  math.ceil((100-self.discount)*self.actual_price/100)

    # def city_name(self):
        # return self.location.split(",")[-2]
# 

class UserInfo(models.Model):
    name  = models.CharField(max_length=40)
    email = models.EmailField(max_length=10)

