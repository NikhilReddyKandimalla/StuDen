# Generated by Django 2.0.13 on 2024-02-23 10:10

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='UserRegisterModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.CharField(max_length=100)),
                ('pswd', models.CharField(max_length=100)),
                ('username', models.CharField(max_length=100)),
                ('mobile', models.CharField(max_length=100)),
                ('studentid', models.CharField(max_length=100)),
                ('university', models.CharField(max_length=100)),
                ('city', models.CharField(max_length=100)),
                ('state', models.CharField(max_length=100)),
                ('country', models.CharField(max_length=100)),
            ],
        ),
    ]
