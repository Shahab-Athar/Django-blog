# Generated by Django 5.0.6 on 2024-05-29 10:09

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0019_auto_20201209_1916'),
    ]

    operations = [
        migrations.AlterField(
            model_name='about',
            name='description',
            field=ckeditor.fields.RichTextField(blank=True, null=True),
        ),
    ]
