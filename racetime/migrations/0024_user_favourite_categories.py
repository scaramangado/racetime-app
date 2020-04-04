# Generated by Django 3.0.2 on 2020-04-04 12:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('racetime', '0023_auto_20200402_1613'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='favourite_categories',
            field=models.ManyToManyField(limit_choices_to={'active': True}, related_name='_user_favourite_categories_+', to='racetime.Category'),
        ),
    ]
