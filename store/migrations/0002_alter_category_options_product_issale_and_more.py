# Generated by Django 5.1.3 on 2024-12-05 04:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'verbose_name_plural': 'Categories'},
        ),
        migrations.AddField(
            model_name='product',
            name='isSale',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='product',
            name='salePrice',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=14),
        ),
    ]
