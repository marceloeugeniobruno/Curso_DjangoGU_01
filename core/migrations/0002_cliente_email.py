# Generated by Django 3.0.8 on 2020-07-30 01:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='cliente',
            name='email',
            field=models.EmailField(default='@gmail', max_length=100, verbose_name='E-mail'),
            preserve_default=False,
        ),
    ]
