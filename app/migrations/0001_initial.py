# Generated by Django 5.0.3 on 2024-06-10 11:06

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='School',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sname', models.CharField(max_length=100)),
                ('sloc', models.CharField(max_length=100)),
                ('scollege', models.CharField(max_length=100)),
            ],
        ),
    ]
