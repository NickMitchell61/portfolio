# Generated by Django 4.0.4 on 2022-05-16 15:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0011_remove_post_url_alter_post_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='date',
            field=models.DateField(),
        ),
    ]