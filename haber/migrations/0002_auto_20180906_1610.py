# Generated by Django 2.1 on 2018-09-06 13:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('haber', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='slug',
            field=models.SlugField(editable=False, max_length=130, unique=True),
        ),
    ]
