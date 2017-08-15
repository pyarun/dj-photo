# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.http.response import HttpResponse
from django.shortcuts import render, render_to_response


# Create your views here.


def hello(request, *args, **kwargs):
    context = {
        "name": "Kalyan"
    }
    return render_to_response('helloWorld.html', context)

    # return HttpResponse("Hello World")