
from .common import StockSerializer

from stock_review.serializers.common import Stock_reviewSerialiser

from category.serializers.common import CategorySerializer

from jwt_auth.serializers.common import UserSerializer

#--------------------------------DEFINE SERIALISER CLASS FOR ASSOCIATED APPS------------------------------# 

# Define PopulatedStockSerializer class, inherited from StockSerializer
class PopulatedStockSerializer(StockSerializer):

    # Define stock_review attribute using Stock_reviewSerialiser to handle multiple related stock reviews
    stock_review = Stock_reviewSerialiser(many=True)
    
    # Define categories attribute using CategorySerializer to handle multiple related categories
    categories = CategorySerializer(many=True)

    # Define owner attribute using UserSerializer, representing user who owns the stock
    owner = UserSerializer()