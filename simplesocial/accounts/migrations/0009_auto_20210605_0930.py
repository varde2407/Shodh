# Generated by Django 3.2.4 on 2021-06-05 09:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0008_auto_20210605_0925'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='linkedin',
            field=models.CharField(default=None, max_length=256, null=True),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='photo',
            field=models.ImageField(default=None, null=True, upload_to=''),
        ),
    ]