# Generated by Django 3.2.8 on 2021-12-27 06:18

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='FormDetails',
            fields=[
                ('usn', models.CharField(max_length=50, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50)),
                ('age', models.PositiveIntegerField()),
                ('stream', models.CharField(max_length=50)),
                ('section', models.CharField(max_length=50)),
            ],
            options={
                'verbose_name': 'FormDetails',
                'verbose_name_plural': 'FormDetailss',
            },
        ),
    ]
