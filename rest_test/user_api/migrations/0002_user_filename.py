# Generated by Django 3.1.4 on 2020-12-21 03:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_api', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='filename',
            field=models.CharField(max_length=256, null=True),
        ),
    ]
