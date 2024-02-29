# Generated by Django 4.2.9 on 2024-02-09 09:00

import Post.models
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Post', '0008_likes'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='picture',
        ),
        migrations.CreateModel(
            name='PostFileContent',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file', models.FileField(upload_to=Post.models.user_directory_path)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='content_owner', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='post',
            name='picture',
            field=models.ManyToManyField(related_name='contents', to='Post.postfilecontent'),
        ),
    ]
