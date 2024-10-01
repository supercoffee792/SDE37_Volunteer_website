# Generated by Django 5.1.1 on 2024-09-28 19:57

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('date', models.DateField(default=datetime.date.today)),
                ('location', models.CharField(max_length=200)),
                ('urgency', models.CharField(choices=[('very_urgent', 'Very urgent'), ('urgent', 'Urgent'), ('not_urgent', 'Not urgent')], default='not_urgent', max_length=20)),
                ('skills', models.TextField(blank=True)),
                ('description', models.TextField(blank=True)),
            ],
        ),
    ]