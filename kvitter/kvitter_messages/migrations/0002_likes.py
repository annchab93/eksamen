from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('kvitter_messages', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='message',
            options={'ordering': ['-id']},
        ),
        migrations.AddField(
            model_name='message',
            name='likes',
            field=models.PositiveIntegerField(default=0),
        ),
    ]