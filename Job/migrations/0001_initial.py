# Generated by Django 3.2.4 on 2022-04-01 05:37

from django.db import migrations, models
import django.db.models.deletion
import django.db.models.manager
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Users', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Jobs',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=100, null=True)),
                ('experience', models.CharField(blank=True, max_length=30, null=True)),
                ('description', models.TextField(blank=True, max_length=2000, null=True)),
                ('Responsibility', models.TextField(blank=True, max_length=2000, null=True)),
                ('qualification', models.TextField(blank=True, max_length=2000, null=True)),
                ('job_type', models.CharField(blank=True, max_length=30, null=True)),
                ('salary', models.DecimalField(blank=True, decimal_places=0, max_digits=10, null=True)),
                ('location', models.CharField(blank=True, max_length=30, null=True)),
                ('slug', models.SlugField(max_length=250, unique_for_date='publish')),
                ('publish', models.DateTimeField(default=django.utils.timezone.now)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('status', models.CharField(choices=[('draft', 'Draft'), ('published', 'Published')], default='draft', max_length=15)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='job_Author', to='Users.profile')),
            ],
            options={
                'ordering': ('-publish',),
            },
            managers=[
                ('published', django.db.models.manager.Manager()),
            ],
        ),
        migrations.CreateModel(
            name='Candidates',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, null=True)),
                ('dob', models.DateField(null=True)),
                ('gender', models.CharField(choices=[('Male', 'male'), ('Female', 'female'), ('Other', 'other')], max_length=200, null=True)),
                ('mobile', models.CharField(max_length=200, null=True)),
                ('email', models.CharField(max_length=200, null=True)),
                ('resume', models.FileField(null=True, upload_to='')),
                ('cover', models.TextField()),
                ('job', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='applied', to='Job.jobs')),
            ],
        ),
    ]
