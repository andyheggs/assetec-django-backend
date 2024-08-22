from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=100, unique=True, help_text="Name of the category, e.g., Technology")

    def __str__(self):
        return self.name


# Technology
# Healthcare
# Finance
# Consumer Services
# Consumer Goods
# Industrial Goods
# Utilities
# Basic Materials
# Energy
# Telecommunications
# Real Estate