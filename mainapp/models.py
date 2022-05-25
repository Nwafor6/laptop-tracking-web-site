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
	lab_name=models.CharField(max_length=250)
	slug=models.SlugField()
	building_num=models.PositiveSmallIntegerField(default=0)
	floor_num=models.PositiveSmallIntegerField(default=1)
	capacity=models.PositiveIntegerField(default=0)
	total_pc=models.PositiveIntegerField( default=0)
	chairs=models.PositiveIntegerField(default=0)
	status=models.CharField(max_length=20, choices=Labouratory_status)

	def __str__(self):
		return f"{self.lab_name} | {self.status}"

	def save(self, *args, **kwargs):
		if not self.slug:
			self.slug=slugify(self.lab_name)
		super(Labouratory, self).save(*args, **kwargs)

class PC(models.Model):

	labouratory=models.ForeignKey(Labouratory, on_delete=models.CASCADE)
	pc_name=models.CharField(max_length=100)
	slug=models.SlugField()
	repaired=models.BooleanField()
	

	def __str__(self):
		return f"{self.pc_name}"

	def save(self, *args, **kwargs):
		if not self.slug:
			self.slug=slugify(self.pc_name)
		super(PC, self).save(*args, **kwargs)

class ReportPc(models.Model):
	Pro_type=[
		('Hardware', 'Hardware'),
		('Software', 'Software')
	]
	labouratory=models.ForeignKey(Labouratory, on_delete=models.CASCADE)
	Number_of_pc=models.PositiveIntegerField(default=1)
	pc_problem=models.TextField(blank=True)
	problem_type=models.CharField(max_length=10, choices=Pro_type)
	date=models.DateTimeField()
	

	def __str__(self):
		return f"{self.pc_problem}"