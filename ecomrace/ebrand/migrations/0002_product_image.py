# Generated by Django 4.2.1 on 2023-09-13 16:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ebrand', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]
