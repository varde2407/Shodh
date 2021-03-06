# Generated by Django 3.0.3 on 2021-05-15 10:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='name',
            field=models.TextField(default=None, null=True),
        ),
        migrations.AddField(
            model_name='post',
            name='year',
            field=models.CharField(choices=[('1', '1st year'), ('2', '2nd year'), ('3', '3rd year'), ('4', '4th year'), ('na', 'Not Applicable')], default='na', max_length=255, null=True),
        ),
    ]
