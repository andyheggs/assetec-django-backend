from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .serializers.common import Stock_reviewSerialiser
from .models import Stock_review
from utils.decorators import handle_exceptions
from utils.permissions import IsOwnerOrReadOnly

#------------------------------------------CREATE ROUTE-----------------------------------------#

# Create View for Stock_review
class Stock_reviewCreateView(APIView):
    # Require user to be authed to access view
    permission_classes = [IsAuthenticated]

    # Decorator to handle exceptions gracefully
    @handle_exceptions  
    def post(self, request):

        request.data['owner'] = request.user.id

        # Serialise incoming request data
        stock_review_to_create = Stock_reviewSerialiser(data=request.data)

        # Check serialised data is valid
        if stock_review_to_create.is_valid():

            # Save valid data to DB
            stock_review_to_create.save()

            # Return created review data with 201
            return Response(stock_review_to_create.data, 201)

          # Return errors with 400 if data invalid
        return Response(stock_review_to_create.errors, 400)  

#----------------------------------------DELETE/DESTROY ROUTE-----------------------------------#

# Delete View for Stock_review
class Stock_reviewDestroyView(APIView):
    # Require user to be owner of the obj or read-only
    permission_classes = [IsOwnerOrReadOnly]

    # Decorator to handle exceptions gracefully
    @handle_exceptions  
    def delete(self, request, pk):

        # Retrieve stock review to delete by primary key
        stock_review_to_delete = Stock_review.objects.get(pk=pk)

        # Check if  user has right permissions to delete obj
        self.check_object_permisisons(request, stock_review_to_delete)

        # Delete retrieved review
        stock_review_to_delete.delete()

        # Return no content status after successful deletion
        return Response(status=204)  
