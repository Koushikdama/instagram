# Generated by Django 4.2.9 on 2024-02-10 06:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authy', '0011_alter_profile_created_at'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='auth_token',
            field=models.CharField(max_length=100),
        ),
    ]
