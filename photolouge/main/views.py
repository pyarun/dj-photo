# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.http.response import HttpResponse, Http404, HttpResponseNotFound
from django.shortcuts import render, render_to_response, redirect


# Create your views here.
from django.urls.base import reverse, reverse_lazy
from django.views.generic.base import View, TemplateView, RedirectView
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView


def hello(request, *args, **kwargs):
    context = {
        "name": "Kalyan"
    }
    # return render_to_response('helloWorld.html', context)
    raise Http404("exception")
    # return HttpResponseNotFound("Hello World")


def redirect_toHello(request, *args, **kwargs):
    url = reverse("hello-abc")
    return redirect(url)



class HelloWorldView(View):

    def get(self, request, *args, **kwargs):
        context = {
            "name": "Kalyan"
        }
        # return render_to_response('helloWorld.html', context)
        return HttpResponse("Hello Class World")


class HelloTemplateView(TemplateView):
    template_name = "helloWorld.html"

    def get_context_data(self, **kwargs):
        kwargs = super(HelloTemplateView, self).get_context_data(**kwargs)
        print kwargs
        kwargs['name']= 'Kalyan'
        return kwargs


class HelloRedrictView(RedirectView):
    # url = 'hello-template'
    url = reverse_lazy('hello-template')

    # def get_redirect_url(self, *args, **kwargs):
    #     return reverse('hello-template')



class ListUsersView(DetailView):
    template_name ="listUsers.html"

    def get_queryset(self):
        return ['Arun'] * 50

    def get_object(self):
        return {
            "name": "Arun",
            "last": "Mittal"
        }






