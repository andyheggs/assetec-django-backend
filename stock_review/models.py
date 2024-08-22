from django.db import models

# Definition of Stock_review model
class Stock_review(models.Model):

    # A text field to store content of review, with a maximum length of 250 characters
    text = models.TextField(max_length=250)

    # A timestamp to record when review was created, automatically set when object is first created
    created_at = models.DateField(auto_now_add=True)

    # A timestamp to record when review was last updated, automatically set to current time on each update
    updated_at = models.DateTimeField(auto_now=True)

    # A foreign key to associate review with a specific stock
    # defined in 'equities.Stock' model. When associated stock is deleted, review will be deleted as well.
    stock = models.ForeignKey(
        # Reference to the 'Stock' model in the 'equities' app
        'equities.Stock',  
        # Cascade delete: This review will be deleted if the associated stock is deleted
        on_delete=models.CASCADE,  
        # Name of the reverse relationship from 'Stock' to 'Stock_review'
        related_name='stock_review'  
    )

    owner = models.ForeignKey(
        'jwt_auth.User',
        on_delete=models.CASCADE,
        related_name='reviews_created'        
    )

        #update stock title field in server to display more relevant information:

    def __str__(self):

        return f' {self.text} - {self.created_at}'

