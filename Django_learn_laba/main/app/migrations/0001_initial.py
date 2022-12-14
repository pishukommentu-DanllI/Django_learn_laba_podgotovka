# Generated by Django 4.1.2 on 2022-12-14 08:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Dishes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('compound', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Hall',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('info', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('customer_name', models.CharField(max_length=50)),
                ('date', models.DateField()),
                ('times_day', models.CharField(max_length=100)),
                ('people_count', models.IntegerField()),
                ('dishes', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.dishes')),
                ('hall', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.hall')),
            ],
        ),
    ]
