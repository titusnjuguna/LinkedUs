# Generated by Django 3.2.4 on 2022-04-04 09:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Job', '0002_jobs_total_opening'),
    ]

    operations = [
        migrations.AddField(
            model_name='jobs',
            name='applicants',
            field=models.ManyToManyField(to='Job.Candidates'),
        ),
    ]
