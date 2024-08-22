from django.urls import path
from .views import StockListCreateView, StockRetrieveUpdateDestroyView

# Define the URL patterns for the stock-related views
urlpatterns = [
    # This URL pattern directs requests with an empty path 
    # to the StockListCreateView, handling GET and POST requests
    path('', StockListCreateView.as_view()),  # /stock/

    # This URL pattern includes a variable path component <int:pk>, 
    # which captures an integer and passes it as a keyword argument pk 
    # to the StockRetrieveUpdateDestroyView, handling GET, PUT, PATCH, and DELETE requests
    path('<int:pk>/', StockRetrieveUpdateDestroyView.as_view())  # /stocks/:id/
]