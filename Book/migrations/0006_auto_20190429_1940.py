# Generated by Django 2.2 on 2019-04-29 11:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Book', '0005_user_is_active'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='is_active',
            field=models.BooleanField(default=False),
        ),
    ]