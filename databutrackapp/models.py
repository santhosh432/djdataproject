from django.db import models

# Create your models here.

import django

priority_levels = (('L','LOW'),
          ('M','MEDIUM'),
          ('H','HIGH'),)

class Bugtrack(models.Model):
    description = models.CharField(max_length=200)
    assign_to = models.CharField(max_length=10)
    created_by = models.CharField(max_length=20)
    priority = models.CharField(max_length=2,choices=priority_levels)
    created_on = models.DateField(default=django.utils.timezone.now,blank=True)

    def __str__(self):
        return self.description
