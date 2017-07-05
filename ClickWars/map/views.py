# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.

def mainmap(request):
	return render(request, 'map/mainmap.html', locals())

def pod(request):
	"""Vue du pod (lieu principal dans lequel les utilisateurs consultent et jouent avec la carte du monde """
	return render(request, 'map/pod.html', locals())

def biodivmap(request):
	"""Vue de la carte de test avec mapbox pour biodivgo"""
	return render(request, 'map/biodivmap.html', locals())
