# Generated by Django 4.2.1 on 2023-06-01 18:10

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
            name='Dog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('breed', models.CharField(max_length=100)),
                ('description', models.TextField(max_length=250)),
                ('age', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Toy',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('color', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Feeding',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(verbose_name='feeding date')),
                ('meal', models.CharField(choices=[('B', 'Breakfast'), ('L', 'Lunch'), ('D', 'Dinner')], default='B', max_length=1)),
                ('dog', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main_app.dog')),
            ],
            options={
                'ordering': ['-date'],
            },
        ),
        migrations.AddField(
            model_name='dog',
            name='toys',
            field=models.ManyToManyField(to='main_app.toy'),
        ),
        migrations.AddField(
            model_name='dog',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
