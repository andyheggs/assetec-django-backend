# Generated by Django 5.1 on 2024-08-19 12:44

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('equities', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Stock_review',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField(max_length=250)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('stock', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='stock_reviews', to='equities.stock')),
            ],
        ),
    ]
