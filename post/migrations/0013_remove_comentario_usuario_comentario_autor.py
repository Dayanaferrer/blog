# Generated by Django 4.2.11 on 2024-04-16 01:23

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('post', '0012_alter_comentario_usuario'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comentario',
            name='usuario',
        ),
        migrations.AddField(
            model_name='comentario',
            name='autor',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
    ]
