from django.db import models
from django.contrib.auth.models import User
from django.utils.text import slugify

# Create your models here.


class Labouratory(models.Model):
	Labouratory_status=[
	('Active', 'Active'),
	('Under maintenance', 'Under maintenance')
]


	user=models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
	lab_name=models.CharField(max_length=250, help_text='Note:Labouratory name must be unique!!')
	slug=models.SlugField(unique=True)
	building_num=models.PositiveSmallIntegerField(help_text='Labouratory Building umber')
	floor_num=models.PositiveSmallIntegerField(help_text='Labouratory floor number')
	capacity=models.PositiveIntegerField(help_text='Labouratory capacity')
	chairs=models.PositiveIntegerField(help_text='Number of chairs in the Labouratory')
	chairs=models.PositiveIntegerField(help_text='Number of PCs in the Labouratory', default=0)
	status=models.CharField(max_length=20, choices=Labouratory_status)

	def __str__(self):
		return f"{self.lab_name} | {self.status}"

	def save(self):
		if not self.slug:
			self.slug=slugify(self.lab_name)
			super(Labouratory, self).save(*args, **kwargs)

class PC(models.Model):

	Pc_Status=[
		('Repaired', 'Repaired'),
		('Damaged', 'Damaged')
	]
	labouratory=models.ForeignKey(Labouratory, on_delete=models.CASCADE)
	pc_name=models.CharField(max_length=100)
	slug=models.SlugField(unique=True)
	status=models.CharField(max_length=10, choices=Pc_Status)

	def __str__(self):
		return f"{self.pc_name} | {self.status}"

	def save(self):
		if not self.slug:
			self.slug=slugify(self.pc_name)
			super(PC, self).save(*args, Kwargs)

class ReportPc(models.Model):
	pc=models.ForeignKey(PC, on_delete=models.CASCADE)
	pc_problem=models.TextField(blank=True)
	date=models.DateTimeField()
	repaired=models.BooleanField(default=False)

	def __str__(self):
		return f"{self.pc_problem} | {self.repaired}"