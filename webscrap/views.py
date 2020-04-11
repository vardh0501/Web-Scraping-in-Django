# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import os
from django.core.management.base import BaseCommand
from bs4 import BeautifulSoup
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
import urllib.request as url

def index(request):
    if request.method == 'GET':
        return render(request,"index.html",locals())
    else:
        new_link = request.POST.get("link")
        page = url.urlopen(new_link)
        soup = BeautifulSoup(page,"lxml")
        images = soup.find_all("img")
        var = []
        for i in images:
            var.append(i)
        return HttpResponse(var)
    





