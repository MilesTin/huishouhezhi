# Generated by Django 2.2 on 2019-04-12 13:31

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='heZhi',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False, unique=True)),
                ('iconPath', models.CharField(max_length=200)),
                ('latitude', models.FloatField()),
                ('longitude', models.FloatField()),
                ('width', models.FloatField()),
                ('height', models.FloatField()),
                ('name', models.CharField(max_length=200)),
                ('address', models.CharField(max_length=200)),
            ],
        ),
    ]
