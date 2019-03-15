# Generated by Django 2.1.7 on 2019-03-15 01:49

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Lectures',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Title', models.CharField(max_length=100)),
                ('Author', models.CharField(max_length=100)),
                ('Content', models.TextField()),
                ('Created_On', models.DateTimeField(auto_now_add=True)),
                ('Updated_At', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
