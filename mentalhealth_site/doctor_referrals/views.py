# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render

from django.http import HttpResponse
from django.template import loader


# Create your views here.

storage = {"Album": [{"id": "www.google.com", "album_title": "album_title_test"}]};
def index(request):
    all_albums = storage["Album"]
    template = loader.get_template("doctor_referrals/index.html")
    context = {
        "all_albums": all_albums()
    }
    return HttpResponse(template.render(context, request))

def detail(request, album_id):
    return HttpResponse()


