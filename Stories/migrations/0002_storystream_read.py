# Generated by Django 4.2.9 on 2024-02-20 15:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Stories', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='storystream',
            name='read',
            field=models.BooleanField(default=False),
        ),
    ]
