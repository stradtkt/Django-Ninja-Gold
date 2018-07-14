# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect
import random
import datetime
# Create your views here.
def index(request):
    try:
        request.session['gold']
    except KeyError:
        request.session['gold'] = 0
    try:
        request.session['append']
    except KeyError:
        request.session['append'] = []
    return render(request, 'ninja/index.html')

def process(request):
    if request.method == "POST":
        if request.POST['location']== "farm":
            random_gold = random.randrange(10,20)
            request.session['gold'] += random_gold
            request.session['append'].append("Gained " + str(random_gold) + " gold from the farm. " + "{:%b/%d/%Y, %I:%M:%S}".format(datetime.datetime.now()))
        if request.POST['location'] == "cave":
            random_gold = random.randrange(5,10)
            request.session['gold'] += random_gold
            request.session['append'].append("Gained " + str(random_gold) + " gold from the cave. " + "{:%b/%d/%Y, %I:%M:%S}".format(datetime.datetime.now()))
        if request.POST['location'] == "house":
            random_gold = random.randrange(2,5)
            request.session['gold'] += random_gold
            request.session['append'].append("Gained " + str(random_gold) + " gold from the house. " + "{:%b/%d/%Y, %I:%M:%S}".format(datetime.datetime.now()))
        if request.POST['location'] == "casino":
            random_gold = random.randrange(5,10)
            request.session['gold'] += random_gold
            request.session['append'].append(str(random_gold) + " gold from the casino. " + "{:%b/%d/%Y %I:%M:%S}".format(datetime.datetime.now()))
        else:
            return redirect('/')
    return redirect('/')


def reset(request):
    request.session.clear()
    return redirect('/')