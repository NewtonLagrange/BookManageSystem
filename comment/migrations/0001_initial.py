# Generated by Django 2.2 on 2019-04-29 06:40

from django.db import migrations, models
import tinymce.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Book', '0004_userimg'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', tinymce.models.HTMLField()),
                ('user', models.ForeignKey(on_delete=None, to='Book.User')),
            ],
        ),
    ]
