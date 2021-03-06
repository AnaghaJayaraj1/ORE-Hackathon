# Generated by Django 3.1.3 on 2020-11-07 05:00

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
            name='Profile1',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('gender', models.CharField(default='NULL', max_length=500, verbose_name='Gender')),
                ('dob', models.CharField(default='NULL', max_length=500, verbose_name='Date Of Birth')),
                ('qualification', models.CharField(default='NULL', max_length=500, verbose_name='Educational Qualification')),
                ('designation', models.CharField(default='NULL', max_length=50, verbose_name='Designation')),
                ('address', models.CharField(default='NULL', max_length=500, verbose_name='Address')),
                ('phone_no', models.CharField(default='NULL', max_length=15, verbose_name='Phone')),
                ('lsgd', models.CharField(default='NULL', max_length=50, verbose_name='LSGD')),
                ('recent_application', models.CharField(default='NULL', max_length=500, verbose_name='Recent Application')),
                ('total_apps', models.CharField(default='NULL', max_length=500, verbose_name='Total Applications')),
                ('entered_apps', models.CharField(default='NULL', max_length=500, verbose_name='Entered Applications')),
                ('verified_apps', models.CharField(default='NULL', max_length=500, verbose_name='Verified Applications')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
