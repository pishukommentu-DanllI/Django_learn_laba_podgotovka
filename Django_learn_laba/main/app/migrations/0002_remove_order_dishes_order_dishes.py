# Generated by Django 4.1.2 on 2022-12-14 08:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='dishes',
        ),
        migrations.AddField(
            model_name='order',
            name='dishes',
            field=models.ManyToManyField(blank=True, null=True, to='app.dishes', verbose_name='Dishes'),
        ),
    ]
