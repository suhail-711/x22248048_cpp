# Generated by Django 5.1.6 on 2025-03-04 17:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0002_booksdb'),
    ]

    operations = [
        migrations.CreateModel(
            name='BackendUserDB',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=100, null=True)),
                ('email', models.EmailField(blank=True, max_length=100, null=True)),
                ('password', models.CharField(blank=True, max_length=100, null=True)),
            ],
        ),
    ]
