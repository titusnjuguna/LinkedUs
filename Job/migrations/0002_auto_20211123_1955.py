# Generated by Django 3.2.4 on 2021-11-23 19:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Job', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='jobs',
            options={'ordering': ('-publish',)},
        ),
        migrations.AddField(
            model_name='jobs',
            name='slug',
            field=models.SlugField(default=1900, max_length=250, unique_for_date='publish'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='jobs',
            name='status',
            field=models.CharField(choices=[('draft', 'Draft'), ('published', 'Published')], default='draft', max_length=15),
        ),
    ]
