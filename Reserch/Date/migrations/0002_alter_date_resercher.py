# Generated by Django 4.1.5 on 2023-02-14 17:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Date', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='date',
            name='resercher',
            field=models.CharField(blank=True, max_length=200, null=True, verbose_name='Исследователь'),
        ),
    ]
