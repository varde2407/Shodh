# Generated by Django 3.2.4 on 2021-06-05 09:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0007_userprofile_username'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='aboutme',
            field=models.TextField(default=None, null=True),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='branch',
            field=models.CharField(choices=[('bt', 'Biotech'), ('ch', 'Chemical'), ('cse', 'Computer Science'), ('mnc', 'Mathematics'), ('ep', 'Engineering Physics'), ('ece', 'Electronics'), ('ee', 'Electrical'), ('me', 'Mechanical'), ('cv', 'Civil'), ('cst', 'CST')], default='bt', max_length=255),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='cpi',
            field=models.FloatField(default=None, null=True),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='gender',
            field=models.CharField(choices=[('anon', 'Prefer Not To Say'), ('m', 'Male'), ('f', 'Female')], default='anon', max_length=255),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='name',
            field=models.CharField(default=None, max_length=256, null=True),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='position',
            field=models.CharField(choices=[('prof', 'Faculty'), ('stud', 'Student'), ('alumnus', 'Alumnus')], default='stud', max_length=255),
        ),
    ]
