# Generated by Django 2.1 on 2018-09-09 15:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('proje', '0002_auto_20180907_0158'),
    ]

    operations = [
        migrations.AlterField(
            model_name='projefoto',
            name='proje',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='projeresimler', to='proje.Proje'),
        ),
    ]
