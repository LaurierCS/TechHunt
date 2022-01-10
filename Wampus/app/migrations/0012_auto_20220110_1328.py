# Generated by Django 3.1.5 on 2022-01-10 17:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0011_profile_category'),
    ]

    operations = [
        migrations.RenameField(
            model_name='category',
            old_name='project',
            new_name='projects',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='category',
        ),
        migrations.AddField(
            model_name='project',
            name='categories',
            field=models.ManyToManyField(blank=True, to='app.Category'),
        ),
    ]
