from attr import fields
from rest_framework.serializers import ModelSerializer

from ..models import Veiculo

class VeiculoSerializer(ModelSerializer):
    class Meta:
      model = Veiculo
      fields = '__all__'