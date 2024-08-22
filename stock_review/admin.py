# Import the necessary modules from Django
from django.contrib import admin
# Import the Stock_review model from the current package's models module
from .models import Stock_review

# Register the Stock_review model with the Django admin site
# This allows us to manage stock reviews through the Django admin interface
admin.site.register(Stock_review)
