# Generated by Django 3.2.9 on 2022-05-25 05:51

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Labouratory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('lab_name', models.CharField(max_length=250)),
                ('slug', models.SlugField(unique=True)),
                ('building_num', models.PositiveSmallIntegerField(default=0)),
                ('floor_num', models.PositiveSmallIntegerField(default=1)),
                ('capacity', models.PositiveIntegerField(default=0)),
                ('total_pc', models.PositiveIntegerField(default=0)),
                ('chairs', models.PositiveIntegerField(default=0)),
                ('status', models.CharField(choices=[('Active', 'Active'), ('Under maintenance', 'Under maintenance')], max_length=20)),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='ReportPc',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Number_of_pc', models.PositiveIntegerField(default=1)),
                ('pc_problem', models.TextField(blank=True)),
                ('problem_type', models.CharField(choices=[('Hardware', 'Hardware'), ('Software', 'Software')], max_length=10)),
                ('date', models.DateTimeField()),
                ('labouratory', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainapp.labouratory')),
            ],
        ),
        migrations.CreateModel(
            name='PC',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pc_name', models.CharField(max_length=100)),
                ('slug', models.SlugField(unique=True)),
                ('repaired', models.BooleanField()),
                ('labouratory', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainapp.labouratory')),
            ],
        ),
    ]
