# Generated by Django 3.1.7 on 2021-03-11 06:17

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Details',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False)),
                ('trainer_name', models.CharField(max_length=30)),
                ('student_name', models.CharField(max_length=30)),
                ('mob_no', models.CharField(max_length=10)),
                ('course', models.CharField(max_length=30)),
                ('duration', models.CharField(max_length=10)),
                ('time_slot', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Trainer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('email', models.EmailField(max_length=30)),
                ('password', models.CharField(max_length=10)),
                ('role', models.CharField(max_length=30)),
            ],
        ),
    ]
