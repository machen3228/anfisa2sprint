# Generated by Django 3.2.16 on 2025-01-11 16:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ice_cream', '0004_auto_20250111_1654'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='category',
            name='price',
        ),
        migrations.AddField(
            model_name='icecream',
            name='price',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=5),
            preserve_default=False,
        ),
    ]
