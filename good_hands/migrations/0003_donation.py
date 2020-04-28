# Generated by Django 3.0.5 on 2020-04-28 09:58

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('good_hands', '0002_institution'),
    ]

    operations = [
        migrations.CreateModel(
            name='Donation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField()),
                ('address', models.CharField(max_length=128)),
                ('phone_number', models.CharField(max_length=32)),
                ('city', models.CharField(max_length=64)),
                ('zip_code', models.CharField(max_length=32)),
                ('pick_up_date', models.DateField()),
                ('pick_up_time', models.TimeField()),
                ('pick_up_comment', models.TextField()),
                ('categories', models.ManyToManyField(to='good_hands.Category')),
                ('institution', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='good_hands.Institution')),
                ('user', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
