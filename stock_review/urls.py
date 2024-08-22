# Importing the path function from django.urls module
from django.urls import path

# Importing the views for creating and destroying stock reviews  
from .views import Stock_reviewCreateView, Stock_reviewDestroyView  

# Define the URL patterns for the stock review views
urlpatterns = [

    # URL pattern for creating a new stock review; matches the root URL
    path('', Stock_reviewCreateView.as_view()),

     # URL pattern for destroying a stock review; matches URLs with an integer primary key  
    path('<int:pk>/', Stock_reviewDestroyView.as_view()) 
    
]