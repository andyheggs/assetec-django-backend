from .common import CategorySerializer
from equities.serializers.common import StockSerializer

class PopulatedCategorySerializer(CategorySerializer):
    stocks = StockSerializer(many=True)