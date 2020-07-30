# Generated by Django 3.0.8 on 2020-07-29 20:03

from django.db import migrations, models
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='patient',
            fields=[
                ('p_userid', models.CharField(max_length=20, primary_key=True, serialize=False)),
                ('p_name', models.CharField(blank=True, max_length=200)),
                ('p_email', models.EmailField(blank=True, max_length=254)),
                ('p_pass', models.CharField(max_length=254)),
                ('p_ph', phonenumber_field.modelfields.PhoneNumberField(blank=True, max_length=128, region=None)),
            ],
        ),
    ]