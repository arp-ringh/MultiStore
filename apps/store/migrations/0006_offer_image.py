# Generated by Django 4.0.4 on 2022-09-29 09:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0005_remove_offer_description_remove_offer_image_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='offer',
            name='image',
            field=models.ImageField(default=1, upload_to='offer'),
            preserve_default=False,
        ),
    ]