# Generated by Django 5.1 on 2024-08-20 10:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stock_review', '0002_alter_stock_review_stock'),
    ]

    operations = [
        migrations.AlterField(
            model_name='stock_review',
            name='created_at',
            field=models.DateField(auto_now_add=True),
        ),
    ]
