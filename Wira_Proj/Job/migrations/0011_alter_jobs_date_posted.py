# Generated by Django 3.2.4 on 2021-06-30 11:00

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('Job', '0010_auto_20210630_1048'),
    ]

    operations = [
        migrations.AlterField(
            model_name='jobs',
            name='date_posted',
            field=models.DateTimeField(default=datetime.datetime(2021, 6, 30, 11, 0, 0, 661428, tzinfo=utc)),
        ),
    ]