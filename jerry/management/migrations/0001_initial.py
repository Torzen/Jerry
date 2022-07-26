# Generated by Django 4.0.2 on 2022-07-22 13:41

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='staffs',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=50)),
                ('password', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='staffs_detail',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fullname', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('address', models.CharField(max_length=200)),
                ('number', models.CharField(max_length=10)),
                ('nationality', models.CharField(max_length=100)),
                ('photoUrl', models.CharField(max_length=500)),
            ],
        ),
    ]
