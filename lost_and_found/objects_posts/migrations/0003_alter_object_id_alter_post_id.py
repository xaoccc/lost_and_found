# Generated by Django 4.2.11 on 2024-03-27 11:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('objects_posts', '0002_alter_post_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='object',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='post',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
