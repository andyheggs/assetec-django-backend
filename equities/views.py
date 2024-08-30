from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.exceptions import PermissionDenied
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly
from .models import Stock
from .serializers.common import StockSerializer
from .serializers.populated import PopulatedStockSerializer
from utils.decorators import handle_exceptions
from utils.permissions import IsOwnerOrReadOnly

#----------------------------------------------------------INDEX ROUTE------------------------------------------------------#

# Path for this view: /Stocks
class StockListCreateView(APIView):
    permission_classes = [IsAuthenticated]

    # Index Route
    @handle_exceptions
    def get(self, request):
        # Model.find() equivalent
        stocks = Stock.objects.filter(owner=request.user)
        # For multiple results use many=True
        serialized_stocks = StockSerializer(stocks, many=True)
        # Return serialised data in response
        return Response(serialized_stocks.data)

#--------------------------------------------------------CREATE ROUTE--------------------------------------------------------#

    # Create Route
    @handle_exceptions
    def post(self, request):
        request.data['owner'] = request.user.id   
        # Deserialise request data to create a stock instance
        stock_to_create = StockSerializer(data=request.data)

        # Check if provided data is valid
        if stock_to_create.is_valid():
            # Save stock instance to DB
            stock_to_create.save()
            # Return serialised data of created stock with HTTP status 201
            return Response(stock_to_create.data, 201)
        
        # If validation fails, log error and return response with errors
        print('Validation error:', stock_to_create.errors)
        return Response(stock_to_create.errors, 400)

#----------------------------------------------------------RETRIEVE ROUTE--------------------------------------------------------#

# Path for this view: /stocks/<int:id>/
class StockRetrieveUpdateDestroyView(APIView):
    permission_classes = [IsOwnerOrReadOnly]

    # Method: GET
    @handle_exceptions
    def get(self, request, pk):
        # Retrieve single stock record by its primary key (id)
        stock = Stock.objects.get(pk=pk)

        # Serialise stock data with additional populated fields
        serialized_stock = PopulatedStockSerializer(stock)
        # Return serialised data in response
        return Response(serialized_stock.data)
    

#--------------------------------------------------------UPDATE ROUTE-------------------------------------------------------#

    # Method: PUT
    @handle_exceptions
    def put(self, request, pk):
        # Retrieve stock record to be updated by its primary key (id)
        stock_to_update = Stock.objects.get(pk=pk)

        # Check if requesting user has necessary permissions for the stock_to_update object 
        self.check_object_permissions(request, stock_to_update)
        
        # Deserialise request data to update stock instance
        serialized_stock = StockSerializer(stock_to_update, data=request.data, partial=True)
        # Check if provided data is valid
        if serialized_stock.is_valid():
            # Save updated stock instance to database
            serialized_stock.save()
            # Return serialised data of updated stock
            return Response(serialized_stock.data)
        # If validation fails, return a response with errors
        return Response(serialized_stock.errors, 400)

#--------------------------------------------------------DESTROY ROUTE--------------------------------------------------------#    
     
    # Method: DELETE
    @handle_exceptions
    def delete(self, request, pk):
        # Retrieve stock record to be deleted by its primary key (id)
        stock_to_delete = Stock.objects.get(pk=pk)

        # Check if the requesting user has the necessary permissions for the stock_to_delete object 
        self.check_object_permissions(request, stock_to_delete)
        # Delete stock record from database
        stock_to_delete.delete()
        # Return a response indicating stock has been successfully deleted
        return Response(status=204)