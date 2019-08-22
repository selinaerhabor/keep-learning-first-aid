# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
from django.utils import timezone

#First Aid Tip Model
class Firstaidtip(models.Model):
    post_id = models.CharField(max_length=200, default='')
    title = models.CharField(max_length=200, default='')
    tip = models.TextField()
    published_date = models.DateTimeField(blank = True, null = True, default = timezone.now)
    
    def __str__(self):
        return self.title
