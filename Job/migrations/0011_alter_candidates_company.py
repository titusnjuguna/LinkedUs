# Generated by Django 3.2.4 on 2021-09-15 17:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Job', '0010_rename_author_jobs_company'),
    ]

    operations = [
        migrations.AlterField(
            model_name='candidates',
            name='company',
            field=models.ManyToManyField(blank=True, to='Job.Jobs'),
        ),
    ]