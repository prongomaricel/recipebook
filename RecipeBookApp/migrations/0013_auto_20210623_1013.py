# Generated by Django 3.1.6 on 2021-06-23 10:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('RecipeBookApp', '0012_auto_20210623_1012'),
    ]

    operations = [
        migrations.AlterField(
            model_name='creator',
            name='crGender',
            field=models.CharField(choices=[('F', 'Female'), ('M', 'Male'), ('O', 'Others')], default='', help_text='Creator Gender', max_length=1),
        ),
    ]