from rest_framework.viewsets import ModelViewSet

from ..models import Modelo
from ..serializers import ModeloSerializer

class ModeloViewSet (ModelViewSet):
    queryset = Modelo.objects.all()
    serializer_class = ModeloSerializer