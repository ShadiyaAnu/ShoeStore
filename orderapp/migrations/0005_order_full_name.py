# Generated by Django 5.0 on 2024-02-01 07:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orderapp', '0004_alter_order_city'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='full_name',
            field=models.CharField(default='', max_length=50),
            preserve_default=False,
        ),
    ]