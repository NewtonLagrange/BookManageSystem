# Generated by Django 2.2 on 2019-04-29 11:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Book', '0004_userimg'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='is_active',
            field=models.BooleanField(default=True),
            preserve_default=False,
        ),
    ]
