# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('newsarticles', '0005_add_scraperresult'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserCoding',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('date', models.DateTimeField(auto_now=True)),
                ('relevant', models.BooleanField()),
            ],
        ),
        migrations.RemoveField(
            model_name='article',
            name='feedname',
        ),
        migrations.AddField(
            model_name='usercoding',
            name='article',
            field=models.ForeignKey(to='newsarticles.Article'),
        ),
        migrations.AddField(
            model_name='usercoding',
            name='categories',
            field=models.ManyToManyField(to='newsarticles.Category'),
        ),
        migrations.AddField(
            model_name='usercoding',
            name='user',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL),
        ),
    ]
