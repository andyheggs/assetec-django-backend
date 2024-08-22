from rest_framework.views import APIView  # Import base APIView class from Django's REST framework
from rest_framework.response import Response  # Importing Response class for sending HTTP responses
from .models import Category  # Import Category model from local models module
from .serializers.common import CategorySerializer  # ImportCategorySerializer for basic serialisation
from .serializers.populated import PopulatedCategorySerializer  # Import PopulatedCategorySerializer for detailed serialisation
from utils.decorators import handle_exceptions  # Import custom decorator for handling exceptions

#----------------------------------------------------------INDEX ROUTE------------------------------------------------------#

# Defining class-based view for handling Category list API requests
class CategoryListView(APIView):  
    # Applying decorator to handle exceptions in view
    @handle_exceptions
    # Define GET method to handle GET requests  
    def get(self, request):
        # Query all category objects from DB 
        category = Category.objects.all()
        # Serialise category objects using PopulatedCategorySerializer  
        serialized_category = PopulatedCategorySerializer(category, many=True)
        # Return JSON response with serialised data  
        return Response(serialized_category.data)  

