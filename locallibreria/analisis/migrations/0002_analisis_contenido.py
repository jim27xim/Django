# Generated by Django 3.1.2 on 2020-10-30 07:20

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('analisis', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='analisis',
            name='contenido',
            field=ckeditor.fields.RichTextField(default=1),
            preserve_default=False,
        ),
    ]
