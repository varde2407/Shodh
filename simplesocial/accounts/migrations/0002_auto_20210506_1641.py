# Generated by Django 3.1.4 on 2021-05-06 11:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='photo',
            field=models.ImageField(default=None, upload_to=''),
        ),
        migrations.AddField(
            model_name='user',
            name='position',
            field=models.CharField(choices=[('prof', 'PROF'), ('stud', 'STUDENT'), ('alumnus', 'ALUMNUS')], default='stud', max_length=255),
        ),
    ]
