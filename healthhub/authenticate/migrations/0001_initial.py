# Generated by Django 4.2.2 on 2023-11-25 04:16

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_username', models.CharField(max_length=50, null=True)),
                ('user_email', models.EmailField(max_length=20, null=True)),
                ('user_password', models.CharField(max_length=20, null=True)),
                ('user_confirmpassword', models.CharField(max_length=50, null=True)),
            ],
        ),
    ]