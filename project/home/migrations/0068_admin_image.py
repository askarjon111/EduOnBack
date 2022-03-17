# Generated by Django 3.0.9 on 2022-03-17 09:02

from django.db import migrations
import django_resized.forms
import home.models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0067_remove_admin_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='admin',
            name='image',
            field=django_resized.forms.ResizedImageField(blank=True, crop=None, force_format='JPEG', keep_meta=True, null=True, quality=75, size=[200, 200], upload_to=home.models.slugify_upload),
        ),
    ]
