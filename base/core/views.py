# coding: utf-8
from annoying.decorators import render_to
from django.shortcuts import redirect

from .models import Human, Talks
from .forms import TalksForm

@render_to('home.html')
def home(request):
	talks = Talks.objects.all()
	return { 'talks' : talks }

@render_to('current.html')
def current(request):
	current = Human.objects.filter(is_active=True, current=True).first
	form = TalksForm(initial={'human': current})
	if request.POST:
		print('2')
		form = TalksForm(request.POST)
		if form.is_valid():
			talk = form.save(commit=False)
			talk.save()
			return redirect('victim')

	return { 'current' : current, 'form': form }

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
