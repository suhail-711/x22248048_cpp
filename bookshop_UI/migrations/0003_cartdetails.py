# Generated by Django 5.1.6 on 2025-03-02 16:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bookshop_UI', '0002_useraccount'),
    ]

    operations = [
        migrations.CreateModel(
            name='CartDetails',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('customer_name', models.CharField(blank=True, max_length=100, null=True)),
                ('book', models.CharField(blank=True, max_length=100, null=True)),
                ('price', models.IntegerField(blank=True, null=True)),
                ('quantity', models.IntegerField(blank=True, null=True)),
                ('total', models.IntegerField(blank=True, null=True)),
            ],
        ),
    ]
