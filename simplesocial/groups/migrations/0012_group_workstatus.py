# Generated by Django 3.2.4 on 2021-06-05 11:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('groups', '0011_alter_group_vacancy'),
    ]

    operations = [
        migrations.AddField(
            model_name='group',
            name='workstatus',
            field=models.CharField(choices=[('ft', 'Full-Time'), ('pt', 'Part-Time')], default='pt', max_length=255),
        ),
    ]
