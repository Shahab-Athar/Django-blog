# Generated by Django 3.1.3 on 2020-12-05 13:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0008_remove_faq_links'),
    ]

    operations = [
        migrations.CreateModel(
            name='aboutmodel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=120)),
                ('description', models.TextField()),
            ],
        ),
    ]