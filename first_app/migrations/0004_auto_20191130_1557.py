# Generated by Django 2.2.5 on 2019-11-30 10:27

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('first_app', '0003_userprofileinfo'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='User',
            new_name='Userr',
        ),
        migrations.AlterField(
            model_name='userprofileinfo',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL),
        ),
    ]
