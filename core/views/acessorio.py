from rest_framework.viewsets import ModelViewSet

from ..models import Acessorio
from ..serializers import AcessorioSerializer


class AcessorioViewSet(ModelViewSet):
    queryset= Acessorio.objects.all()
    serializer_class= AcessorioSerializer