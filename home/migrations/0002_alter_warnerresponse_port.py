# Generated by Django 4.1.7 on 2023-03-20 16:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='warnerresponse',
            name='port',
            field=models.CharField(max_length=5),
        ),
    ]