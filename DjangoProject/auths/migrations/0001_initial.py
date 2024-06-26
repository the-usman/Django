# Generated by Django 5.0.6 on 2024-06-09 12:58

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Sinup',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('avatar', models.ImageField(upload_to='auth/')),
                ('password', models.CharField(max_length=20)),
                ('username', models.CharField(max_length=20)),
                ('user_type', models.CharField(choices=[('ad', 'admin'), ('us', 'user')], max_length=2)),
                ('createdAt', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
    ]
