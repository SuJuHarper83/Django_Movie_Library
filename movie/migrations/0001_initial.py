# Generated by Django 4.1.3 on 2022-11-21 20:57

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('director', models.CharField(max_length=255)),
                ('genre', models.CharField(max_length=255)),
                ('release_date', models.DateField()),
                ('likes', models.IntegerField(default=0)),
            ],
        ),
    ]
