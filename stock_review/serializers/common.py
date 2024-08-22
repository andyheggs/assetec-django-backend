from rest_framework.serializers import ModelSerializer
from ..models import Stock_review

class Stock_reviewSerialiser(ModelSerializer):
    class Meta:
        model = Stock_review
        fields = '__all__'