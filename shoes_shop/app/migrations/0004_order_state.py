# Generated by Django 5.1.2 on 2024-11-02 05:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_product_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='state',
            field=models.CharField(default='pending', max_length=20),
        ),
    ]
