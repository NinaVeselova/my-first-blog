# Generated by Django 2.0.13 on 2019-07-27 18:08

from django.db import migrations
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_auto_20190724_1601'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='text',
            field=tinymce.models.HTMLField(),
        ),
    ]
