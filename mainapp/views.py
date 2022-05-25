from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.core import serializers
from .models import *
from .forms import *
from django.views.generic import TemplateView, DetailView, ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView

# Create your views here.

class HomePageView(TemplateView):
	template_name='mainapp/home-page.html'

# search section
class LabouratoryTemplateView(ListView):
	model=Labouratory
	template_name='mainapp/labouratory.html'
	# context_object_name='labs'

	def get(self,request, *args, **kwargs):
		q=request.GET.get('q') if request.GET.get('q') !=None else ''
		# products=Market.objects.all()[:3]
		labs=Labouratory.objects.filter(lab_name__icontains=q)
		return render (request, self.template_name, {'labs':labs})

# create a labouratory 
class LabouratoryCreateView(CreateView):
	form_class=CreateLabForm
	model=Labouratory
	template_name='mainapp/create-lab.html'
	success_url='/lab'

	def post (self,request, *args, **kwargs):
		form=CreateLabForm(request.POST)
		if form.is_valid():
			form.instance.user=request.user
			form.save()
		return redirect(self.success_url)

# Edit a labouratory
class LabouratoryUpdateView(UpdateView):
	model=Labouratory
	form_class=CreateLabForm
	template_name='mainapp/create-lab.html'
	success_url='/lab'

class LabouratoryDetailView(DetailView):
	model=Labouratory
	template_name='mainapp/lab-detail.html'
	# context_object_name='report'

	def get_context_data(self,  *args, **kwargs):
		context=super().get_context_data(**kwargs)
		lab=Labouratory.objects.get(slug=self.kwargs['slug'])
		context['pcs']=lab.pc_set.all()
		# context['report']=ReportPc.objects.get(labouratory=lab)
		context['report']=ReportPc.objects.filter(labouratory=lab)
		return context


# delete a labouratory
class LabouratoryDeleteView(DeleteView):
	model=Labouratory
	form_class=CreateLabForm
	template_name='mainapp/Delete a Laboratory.html'
	success_url='/lab'


class File_A_Report(CreateView):
	form_class=ReportPCForm
	model=ReportPc
	template_name='mainapp/report problem page.html'
	success_url='/report-list'

class Update_File_A_Report(UpdateView):
	form_class=ReportPCForm
	model=ReportPc
	template_name='mainapp/report problem page.html'
	success_url='/report-list'


class CreatePc(CreateView):
	form_class=CreatePCForm
	model=PC
	template_name='mainapp/Add a pc.html'
	success_url='/pcs'

	def post(self,request, *args, **kwargs):
		if self.request.is_ajax and self.request.method == "POST":
			form = self.form_class(self.request.POST)
			if form.is_valid():
				instance = form.save()
				ser_instance = serializers.serialize('json', [ instance, ])
				# send to client side.
				# return JsonResponse({"instance": ser_instance}, status=200)
				return redirect(self.success_url)
			else:
				return JsonResponse({"error": form.errors}, status=400)

		return JsonResponse({"error": ""}, status=400)


class UpdatePc(UpdateView):
	form_class=CreatePCForm
	model=PC
	template_name='mainapp/Add a pc.html'
	success_url='/lab'


class PCListView(ListView):
	model=PC
	template_name='mainapp/pcs.html'
	context_object_name='pcs'

class About(TemplateView):
	template_name='mainapp/about.html'

class ReportListView(ListView):
	model=ReportPc
	template_name='mainapp/report-list.html'
	context_object_name='reports'




