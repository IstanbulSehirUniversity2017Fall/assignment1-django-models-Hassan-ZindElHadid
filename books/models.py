# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Book(models.Model):
    author = models.CharField(max_length = 25)
    title = models.CharField(max_length= 30)
    genre = models.CharField(max_length= 15)
    page_count = models.IntegerField()
    date_published = models.DateTimeField()
    def __str__(self):
        return self.title
    
class Chapters(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    chapter_number = models.IntegerField()

