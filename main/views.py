from django.shortcuts import render, render_to_response

# Create your views here.
from main.models import SpeedModel
from django.template import RequestContext
from django.http import HttpResponseRedirect

from main.forms import SpeedModelForm, SpeedModelForm2, SpeedModelUpdateForm

def detail_view(request, pk):

	speed_object = SpeedModel.objects.get(pk=pk)

	context = {}

	context['speed_object'] = speed_object

	return render_to_response('detail_view.html', context, context_instance=RequestContext(request))


def list_view(request):

	speed_objects = SpeedModel.objects.all()

	context = {}

	context['speed_objects'] = speed_objects

	return render_to_response('list_view.html', context, context_instance=RequestContext(request))

def create_view1(request):

	context = {}

	form = SpeedModelForm()
	context['form'] = form

	if request.method == 'POST':
		form = SpeedModelForm(request.POST, request.FILES)
		if form.is_valid():
			form.save()

			return HttpResponseRedirect('/list_view/')

		else:
			context['errors'] = form.errors

	return render_to_response('create_view1.html', context, context_instance=RequestContext(request))

def create_view2(request):

	context = {}

	form = SpeedModelForm2()
	context['form'] = form

	if request.method == 'POST':
		form = SpeedModelForm2(request.POST, request.FILES)

		if form.is_valid():

			print form.cleaned_data

			title = form.cleaned_data['title']
			info = form.cleaned_data['info']
			image = form.cleaned_data['image']

			new_object = SpeedModel()

			new_object.title = title
			new_object.info = info
			new_object.image = image

			new_object.save()

			return HttpResponseRedirect('/list_view/')
		else:
			context['errors'] = form.errors

	return render_to_response('create_view2.html', context, context_instance=RequestContext(request))


def update_view(request, pk):

	context = {}

	speed_object = SpeedModel.objects.get(pk=pk)

	context['speed_object'] = speed_object

	form = SpeedModelUpdateForm()

	context['form'] = form

	if request.method == 'POST':
		form = SpeedModelUpdateForm(request.POST, request.FILES)

		if form.is_valid():
			speed_object.title = form.cleaned_data['title']
			speed_object.info = form.cleaned_data['info']

			if form.cleaned_data['image'] != None:
				speed_object.image = form.cleaned_data['image']

			speed_object.save()

			return HttpResponseRedirect('/update_view/%s/' % pk)

		else:
			context['errors'] = form.errors

	return render_to_response('update_view.html', context, context_instance=RequestContext(request))


def delete_view(request, pk):

	SpeedModel.objects.get(pk=pk).delete()

	return HttpResponseRedirect('/list_view/')



