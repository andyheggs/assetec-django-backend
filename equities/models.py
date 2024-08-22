from django.db import models
from category.models import Category 

# Create your models here.
class Stock(models.Model):

    company_code = models.CharField(max_length=10, unique=True, help_text="Stock ticker symbol, e.g., AAPL")
    company_name = models.CharField(max_length=100, help_text="Full name of the company, e.g., Apple Inc.")
    trade_date = models.DateTimeField(help_text="The date when the stock was traded")
    quantity = models.IntegerField(help_text="Number of shares purchased")
    share_price = models.DecimalField(max_digits=10, decimal_places=2, help_text="Price per share at the time of purchase")
    new_share_price = models.DecimalField(max_digits=10, decimal_places=2, help_text="New Price per share at current time")
    brokerage_fees = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True, help_text="Any brokerage fees associated with the purchase")
    description = models.TextField(null=True, blank=True, help_text="Additional information relevant to the stock")
    last_updated = models.DateTimeField(auto_now=True, help_text="Timestamp when the stock information was last updated")

    owner = models.ForeignKey(
        'jwt_auth.User',
        on_delete=models.CASCADE,
        related_name='stocks_created'        
    )
    
    
    #update stock title field in server to display more relevant information:

    def __str__(self):

        return f' "{self.company_code}" - {self.company_name} - {self.share_price}'



    

