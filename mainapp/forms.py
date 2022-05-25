from django import forms
from .models import *


class CreateLabForm(forms.ModelForm):
	Labouratory_status=[
	('Active', 'Active'),
	('Under maintenance', 'Under maintenance')
]


	status= forms.ChoiceField(widget=forms.RadioSelect(),choices=Labouratory_status, label='')
	class Meta:
		model=Labouratory
		fields=['lab_name','building_num','floor_num','capacity','total_pc','chairs','status']

class CreatePCForm(forms.ModelForm):
	# Pc_Status=[
	# 	('Repaired', 'Repaired'),
	# 	('Damaged', 'Damaged')
	# ]
	# status= forms.ChoiceField(widget=forms.RadioSelect(),choices=Pc_Status, label='')

	class Meta:
		model=PC
		fields=['labouratory','pc_name', 'repaired']

class ReportPCForm(forms.ModelForm):
	Pro_type=[
		('Hardware', 'Hardware'),
		('Software', 'Software')
	]
	date=forms.DateTimeField(widget = forms.SelectDateWidget())
	problem_type= forms.ChoiceField(widget=forms.RadioSelect(),choices=Pro_type, label='')

	class Meta:
		model=ReportPc
		fields=['labouratory','Number_of_pc','pc_problem','problem_type', 'date']