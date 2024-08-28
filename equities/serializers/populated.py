
from .common import StockSerializer

from jwt_auth.serializers.common import UserSerializer

#--------------------------------DEFINE SERIALISER CLASS FOR ASSOCIATED APPS------------------------------# 

# Define PopulatedStockSerializer class, inherited from StockSerializer
class PopulatedStockSerializer(StockSerializer):

    # Define owner attribute using UserSerializer, representing user who owns the stock
    owner = UserSerializer()