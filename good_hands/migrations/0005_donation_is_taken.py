# Generated by Django 3.0.5 on 2020-05-08 09:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('good_hands', '0004_remove_donation_is_taken'),
    ]

    operations = [
        migrations.AddField(
            model_name='donation',
            name='is_taken',
            field=models.BooleanField(default=False),
        ),
    ]