# Generated by Django 4.0.1 on 2022-02-03 05:12

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Documents',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Title', models.CharField(max_length=25)),
                ('Description', models.TextField()),
                ('Attachments', models.FileField(upload_to='Files/')),
                ('Signature', models.CharField(max_length=15)),
                ('datetime', models.DateField(default=datetime.datetime.now)),
            ],
        ),
    ]
