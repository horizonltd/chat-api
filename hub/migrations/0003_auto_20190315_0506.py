# Generated by Django 2.1.7 on 2019-03-15 12:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hub', '0002_auto_20190314_1857'),
    ]

    operations = [
        migrations.RenameField(
            model_name='lecture',
            old_name='Author',
            new_name='author',
        ),
        migrations.RenameField(
            model_name='lecture',
            old_name='Content',
            new_name='content',
        ),
        migrations.RenameField(
            model_name='lecture',
            old_name='Created_On',
            new_name='created_on',
        ),
        migrations.RenameField(
            model_name='lecture',
            old_name='Title',
            new_name='title',
        ),
        migrations.RenameField(
            model_name='lecture',
            old_name='Updated_At',
            new_name='updated_at',
        ),
    ]