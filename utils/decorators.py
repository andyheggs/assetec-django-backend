from equities.models import Stock
from rest_framework.exceptions import NotFound, PermissionDenied
from rest_framework.response import Response

# Decorator function that handles all handler method exceptions
def handle_exceptions(handler_func):

    def wrapper(*args, **kwargs):

        try:

            # Call the handler function with passed arguments
            return handler_func(*args, **kwargs)  
        
        # Handle specific exceptions: Stock.DoesNotExist and NotFound
        except (Stock.DoesNotExist, NotFound) as e:
            
            # Print the type of exception
            print(type(e))  

            # Return a 404 Response with the exception message
            return Response({ 'message': str(e) }, 404)

        # Handle PermissionDenied exception
        except PermissionDenied as e:

            # Print the exception itself
            print(e)

            # Return a 403 Response with the exception message
            return Response({ 'message': str(e) }, 403)
        
        # Handle any other exceptions
        except Exception as e:

            # Print the class name of the exception
            print(e.__class__.__name__)

            # Print the exception itself  
            print(e)

             # Return a 500 Response with generic error message
            return Response('An unknown error occurred', 500) 
        
    return wrapper