# Generated by Django 3.2.4 on 2022-04-04 09:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Job', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='jobs',
            name='total_opening',
            field=models.DecimalField(blank=True, decimal_places=0, max_digits=100, null=True),
        ),
    ]