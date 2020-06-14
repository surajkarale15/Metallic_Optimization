from rest_framework.serializers import ModelSerializer,HyperlinkedModelSerializer
from .models import Commodity,Chemical_composition,Element


class ElementSer(ModelSerializer):
    class Meta:
        model = Element
        fields = ['id','name']
        depth = 1

class CommoditySer(ModelSerializer):
    class Meta:
        model = Commodity
        fields = ['id','name','inventory','price']
        
        
class ChemicalSer(ModelSerializer):
    class Meta:
        model = Chemical_composition
        fields = ['id','comodity','element','percentage']





