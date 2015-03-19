# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0002_auto_20150313_2125'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comments',
            old_name='comment_article',
            new_name='comments_article',
        ),
    ]
