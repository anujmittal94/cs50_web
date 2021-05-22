# Generated by Django 3.1.5 on 2021-05-19 15:05

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('network', '0002_follow_post'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='likes',
            field=models.ManyToManyField(blank=True, related_name='likesonpost', to=settings.AUTH_USER_MODEL),
        ),
    ]
