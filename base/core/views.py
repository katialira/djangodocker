# coding: utf-8
from annoying.decorators import render_to
from django.shortcuts import redirect

from .models import Human, Talks
from .forms import TalksForm


@render_to('home.html')
def home(request):
	talks = Talks.objects.filter(cicle=1)[4:]
	return { 'talks' : talks }


@render_to('current.html')
def current(request):
	current = Human.objects.get(is_active=True, current=True)
	print(current)
	form = TalksForm(initial={'human': current})
	if request.POST:
		form = TalksForm(request.POST)
		if form.is_valid():
			talk = form.save(commit=False)
			talk.cicle = 1
			talk.save()
			return redirect('nominee')

	return { 'current' : current, 'form': form }


@render_to('nominee.html')
def nominee(request):
	nominees = Human.objects.filter(is_active=True, lightning=True)
	if request.POST:
		current = Human.objects.get(is_active=True, current=True)
		current.current = False
		current.save()
		victim = Human.objects.get(pk=request.POST.get('user'))
		victim.current = True
		victim.lightning = False
		victim.save()
		return redirect('home')

	return {'nominees': nominees}


@render_to('victim.html')
def victim(request):
	current = Human.objects.get(is_active=True, current=True)
	victim = Human.objects.filter(is_active=True, lightning=True).order_by('?').first()
	
	current.current = False
	current.save()
	victim.current = True
	victim.lightning = False
	victim.save()

	return { 'current' : current, 'victim': victim }





