# Generated by Django 3.0.9 on 2022-03-17 08:43

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('home', '0065_discount'),
    ]

    operations = [
        migrations.AddField(
            model_name='admin',
            name='promoted_at',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AddField(
            model_name='admin',
            name='promoted_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='promoted_by', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='admin',
            name='status',
            field=models.ManyToManyField(blank=True, to='home.Permissions'),
        ),
    ]
