# Generated by Django 3.1.6 on 2021-06-23 10:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('RecipeBookApp', '0009_remove_creator_crgender'),
    ]

    operations = [
        migrations.AddField(
            model_name='creator',
            name='crGender',
            field=models.CharField(choices=[('F', 'Female'), ('M', 'Male'), ('O', 'Others')], default='', max_length=1),
        ),
    ]
