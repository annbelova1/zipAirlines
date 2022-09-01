# Generated by Django 3.0.8 on 2022-09-01 05:21

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Airplane',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_id', models.PositiveIntegerField(null=True)),
                ('passengers_count', models.PositiveIntegerField(default=0)),
                ('airplane_id', models.PositiveIntegerField(validators=[django.core.validators.MinValueValidator(1)])),
                ('created', models.DateTimeField(auto_now_add=True, help_text='date of creation', verbose_name='created')),
                ('updated', models.DateTimeField(auto_now=True, help_text='profile updated', verbose_name='updated')),
            ],
            options={
                'verbose_name': 'Airplane',
                'verbose_name_plural': 'Airplanes',
                'ordering': ('-created',),
            },
        ),
    ]