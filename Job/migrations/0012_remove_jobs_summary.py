# Generated by Django 3.2.4 on 2021-09-15 17:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Job', '0011_alter_candidates_company'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='jobs',
            name='summary',
        ),
    ]