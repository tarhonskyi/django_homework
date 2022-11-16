# Generated by Django 4.0.6 on 2022-11-15 21:07

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Film',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('producer', models.CharField(max_length=50)),
            ],
            options={
                'verbose_name': 'Фільм',
                'verbose_name_plural': 'Фільми',
                'ordering': ('title',),
            },
        ),
        migrations.CreateModel(
            name='Actor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('surname', models.CharField(max_length=50)),
                ('oskars', models.IntegerField()),
                ('films', models.ManyToManyField(null=True, to='lesson_4.film')),
            ],
            options={
                'verbose_name': 'Актор',
                'verbose_name_plural': 'Актори',
                'ordering': ('name',),
            },
        ),
    ]
