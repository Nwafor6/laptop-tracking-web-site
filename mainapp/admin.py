from django.contrib import admin
from .models import *

# Register your models here.

class LabouratoryAdmin(admin.ModelAdmin):
	list_display=['user', 'lab_name', 'building_num', 'floor_num', 'capacity', 'total_pc', 'chairs', 'status']
	prepopulated_fields={'slug': ('lab_name',)}

class PCAdmin(admin.ModelAdmin):
	list_display=['labouratory', 'pc_name', 'repaired']
	prepopulated_fields={'slug': ('pc_name',)}

class ReportPcAdmin(admin.ModelAdmin):
	list_display=['labouratory','Number_of_pc', 'pc_problem','problem_type', 'date']
	

admin.site.register(Labouratory, LabouratoryAdmin)
admin.site.register(PC, PCAdmin)
admin.site.register(ReportPc, ReportPcAdmin)


