# Generated by Django 5.0 on 2024-01-14 07:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('authy', '0005_otptoken'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='is_private',
        ),
        migrations.DeleteModel(
            name='OtpToken',
        ),
    ]
