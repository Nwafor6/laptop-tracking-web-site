# from .import views
from django.urls import path
from .views import *

urlpatterns = [
   path('', HomePageView.as_view(), name='home'),
   path('lab', LabouratoryTemplateView.as_view(), name='lab'),
   path('create-lab', LabouratoryCreateView.as_view(), name='create-lab'),
   path('update-lab/<slug:slug>', LabouratoryUpdateView.as_view(), name='update-lab'),
   path('delete-lab/<slug:slug>', LabouratoryDeleteView.as_view(), name='delete-lab'),
   path('report-pc', File_A_Report.as_view(), name='report-pc'),
   path('report-pc/<int:pk>/', Update_File_A_Report.as_view(), name='up-report'),
   path('lab/report/<slug:slug>', LabouratoryDetailView.as_view(), name='report'),
   path('create-pc', CreatePc.as_view(), name='create-pc'),
   path('update-pc/<slug:slug>', UpdatePc.as_view(), name='update-pc'),
   path('pcs', PCListView.as_view(), name='pcs'),
   path('about', About.as_view(), name='about'),
   path('report-list', ReportListView.as_view(), name='report-list')
]
