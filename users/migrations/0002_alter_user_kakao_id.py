# Generated by Django 4.0.1 on 2022-02-16 16:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='kakao_id',
            field=models.PositiveIntegerField(null=True),
        ),
    ]
