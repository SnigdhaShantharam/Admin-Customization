# Generated by Django 2.1 on 2020-03-09 12:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('admincust', '0002_auto_20200309_0745'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='description',
            field=models.CharField(max_length=300),
        ),
    ]
