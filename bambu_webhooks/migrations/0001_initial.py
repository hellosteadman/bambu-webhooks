# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Action',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('hash', models.CharField(db_index=True, max_length=100, null=True, blank=True)),
                ('data', models.TextField(null=True, blank=True)),
            ],
            options={
                'db_table': 'webhooks_action',
            },
        ),
        migrations.CreateModel(
            name='Receiver',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('hook', models.CharField(db_index=True, max_length=100, choices=[(b'post_published', b'Post published')])),
                ('url', models.URLField(max_length=255, db_index=True)),
                ('last_called', models.DateTimeField(null=True, blank=True)),
                ('user', models.ForeignKey(related_name='webhooks', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ('hook',),
                'db_table': 'webhooks_receiver',
            },
        ),
        migrations.AddField(
            model_name='action',
            name='receiver',
            field=models.ForeignKey(related_name='actions', to='bambu_webhooks.Receiver'),
        ),
        migrations.AlterUniqueTogether(
            name='receiver',
            unique_together=set([('url', 'hook', 'user')]),
        ),
    ]
