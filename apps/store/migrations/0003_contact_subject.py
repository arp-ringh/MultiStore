# Generated by Django 4.1.3 on 2022-11-27 08:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("store", "0002_contact_slider_offer"),
    ]

    operations = [
        migrations.AddField(
            model_name="contact",
            name="subject",
            field=models.CharField(default=2, max_length=400),
            preserve_default=False,
        ),
    ]
