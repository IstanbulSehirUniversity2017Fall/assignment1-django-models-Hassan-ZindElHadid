# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpRequest
from django.test import TestCase
# Create your views here.


def index(request):
    return HttpResponse("<h1>A response<h1>")

def book_details(request, book_id):
    return HttpResponse("<h2>This is the book number %s<h2>"%str(book_id))

class BookViewsTest(TestCase):
    def test_index(self):
        response = self.client.get(reversed('index'))
        self.assertEqual(response.status_code, 200)

