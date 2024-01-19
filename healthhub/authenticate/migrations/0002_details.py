# Generated by Django 4.2.2 on 2023-12-06 06:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authenticate', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='details',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('st_fullname', models.CharField(max_length=50)),
                ('st_weight', models.IntegerField()),
                ('st_height', models.IntegerField()),
                ('st_age', models.IntegerField()),
                ('st_goal', models.IntegerField()),
                ('st_time', models.IntegerField(null=True)),
            ],
        ),
    ]
