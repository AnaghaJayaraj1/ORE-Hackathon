# Generated by Django 3.1 on 2020-08-16 15:57

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Application',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(max_length=100)),
                ('name', models.CharField(max_length=100)),
                ('typeofcertificate', models.CharField(choices=[('D', 'Death Certificate'), ('B', 'Birth Certificate'), ('R', 'Revenue Certificate'), ('C', 'Contract Certificate')], default='B', max_length=1)),
                ('fileid', models.CharField(max_length=100)),
                ('action', models.CharField(choices=[('N', 'No Action'), ('A', 'Action'), ('V', 'Verified')], default='N', max_length=1)),
            ],
        ),
    ]
