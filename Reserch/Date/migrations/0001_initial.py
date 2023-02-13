# Generated by Django 4.1.5 on 2023-02-13 15:14

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Date',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Дата заполнения')),
                ('name', models.CharField(blank=True, db_index=True, max_length=200, verbose_name='фамилия')),
                ('gender', models.CharField(choices=[(None, 'уточнить пол'), ('m', 'мужской'), ('f', 'женский')], max_length=1, verbose_name='пол')),
                ('age', models.IntegerField(verbose_name='возраст')),
                ('status', models.CharField(choices=[('s', 'холост/не замужем'), ('m', 'в браке'), ('d', 'в разводе'), ('w', 'вдов_а')], max_length=1, verbose_name='социальный статус')),
                ('efficiency', models.DecimalField(blank=True, decimal_places=1, default='some_value', max_digits=4, null=True, verbose_name='эффективность работы')),
                ('workability', models.DecimalField(decimal_places=1, max_digits=4, verbose_name='врабатываемость')),
                ('mentalstab', models.DecimalField(decimal_places=1, max_digits=4, verbose_name='устойчивость')),
                ('IQV', models.IntegerField(verbose_name='IQверб')),
                ('IQN', models.IntegerField(verbose_name='IQневерб')),
                ('iq', models.IntegerField(verbose_name='IQобщ')),
                ('slug', models.SlugField(unique=True)),
                ('resercher', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL, verbose_name='Исследователь')),
            ],
            options={
                'verbose_name': 'исследуемый',
                'verbose_name_plural': 'исследуемые',
            },
        ),
    ]
