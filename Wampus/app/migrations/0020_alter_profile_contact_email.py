# Generated by Django 4.0 on 2022-02-08 07:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0019_alter_profile_contact_email'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='contact_email',
            field=models.EmailField(blank=True, max_length=200, null=True),
        ),
    ]
