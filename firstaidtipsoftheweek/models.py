# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
import datetime

#First Aid Tip Model
class Firstaidtip(models.Model):
    post_id = models.CharField(max_length=200, default='')
    title = models.CharField(max_length=200, default='')
    tip = models.TextField()
    startdate = models.DateField(null = True)
    enddate = models.DateField(null = True)
      
    def __str__(self):
        return "{0}-{1}-{2}".format(self.post_id, self.title, self.startdate)
